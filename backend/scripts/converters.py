from music21 import *
from .billboard_chords import billboard_chord
from .jp_format import estimate_jp_key, convert_to_jp_key
from .factsheet import score_factsheet

class ConverterBillboard(converter.subConverters.SubConverter):
    registerFormats = ('billboard',)
    registerInputExtensions = ('txt',)
    
    def parseData(self, dataString: str, number=None):
        # load in the songs metadata
        meta_str, body_str = dataString.split('\n\n')
        meta_str = meta_str.replace('# ', '')
        metalines = {}
        for line in meta_str.split('\n'):
            split = line.split(': ')
            metalines[split[0]] = split[1]
        self.stream = stream.Score()
        self.stream.metadata = metadata.Metadata(
            title=metalines['title'],
            composer=metalines['artist']
        )
        self.stream.timeSignature = meter.TimeSignature(metalines['metre'])
        if '?' not in metalines['tonic']:
            self.stream.keySignature = key.Key(metalines['tonic'])

        # divide the score into lines
        body_lines = body_str.split('\n')
        # trim of the metadata lines and time markers
        body_lines = [line.split('\t')[-1] for line in body_lines if line[0:1 != '#'] and '|' in line]
        # TODO: check for when special form appears

        # sort the piece into sections as labeled
        sections = []
        current_section = None
        for line in body_lines:
            i = line.index('|')
            if i != 0:
                if current_section: sections.append(current_section)
                current_section = [line[:i].strip(), []]
            measures = [m.strip() for m in line[i:].split('|')][1:]
            if measures[-1]:
                pre_comma = measures[-1].split(',')[0]
                if 'x' in pre_comma:
                    measures = measures[:-1] * int(pre_comma[1:])
            measures = measures[:-1]
            current_section[1] += measures
        if current_section: sections.append(current_section)

        special_time = False
        for section in sections:
            part = stream.Stream()
            part.id = section[0]
            part.keySignature = key.Key(*self.stream.keySignature.name.split())
            for measure in section[1]:
                elements = measure.split()
                # if measure has specified time signature
                time_signature = meter.TimeSignature(self.stream.timeSignature.ratioString)
                if elements[0][0] == '(':
                    elements = elements[1:]
                    time_signature = meter.TimeSignature(measure[:measure.index(')')])
                    part.append(time_signature)
                    special_time = True
                # else use score time signature
                elif special_time:
                    part.append(time_signature)
                    special_time = False
                
                measure_len = time_signature.barDuration.quarterLength
                element_len = measure_len/len(elements)
                for el in elements:
                    # for N, *, &pause: add a rest (with fermata)
                    if el in ('N', '*', '&pause'):
                        rest = note.Rest()
                        rest.quarterLength = element_len 
                        if el == '&pause':
                            rest.expressions.append(expressions.Fermata())
                        part.append(rest)
                    # for .: repeat last chord
                    elif el == '.':
                        # TODO: THIS IS SOMEWHAT JANKY
                        prev = part[-1]
                        part.remove(prev)
                        prev.quarterLength += element_len
                        part.append(prev)
                    # add normal chord annotations
                    else:
                        part.append(billboard_chord(el, element_len))
            part.notesAndRests[0].addLyric(section[0])
            self.stream.append(part)
        
        # analyze key and convert
        self.stream = convert_to_jp_key(self.stream)


class ConverterRollingStone(converter.subConverters.SubConverter):
    registerFormats = ('rs',)
    registerInputExtensions = ('har',)
    
    def parseData(self, dataString: str, number=None):
        # get score using integrated romanText module
        ct_song = romanText.clercqTemperley.CTSong(dataString)
        ct_stream = ct_song.toScore(labelRomanNumerals=False)

        # parse outer sections from the song rule
        form_string = ct_song.rules['S'].musicText
        sections = []
        current_section = None
        for i in range(len(form_string)):
            if form_string[i] == '$':
                current_section = ''
            elif form_string[i] == ' ':
                if current_section != None:
                    sections.append(current_section)
                    current_section = None
            elif current_section != None:
                current_section += form_string[i]
        if current_section != None:
            sections.append(current_section)
            current_section = None

        # expand repeated sections
        expanded_sections = []
        for section in sections:
            if '*' in section:
                index = section.find('*')
                expanded_sections += [section[:index]] * int(section[index+1:])
            else:
                expanded_sections += [section]
        sections = expanded_sections
        
        # make a Score object using the outer structure
        self.stream = stream.Score()
        self.stream.metadata = ct_stream.metadata
        self.stream.timeSignature = ct_song.homeTimeSig
        self.stream.keySignature = key.Key('C')
        target = self.stream
        section_index = 0
        next_section = sections[section_index]
        # add each note element
        for el in ct_stream.recurse().notesAndRests:
            # add new section as a child stream
            if next_section in [l.text for l in el.lyrics]:
                part = stream.Stream()
                part.id = next_section
                part.keySignature = key.Key('C')
                section_index += 1
                if section_index < len(sections): next_section = sections[section_index]
                target = part
                self.stream.append(part)
            # add the element to proper destination
            target.append(el)

        # analyze key and convert
        self.stream = convert_to_jp_key(self.stream)


# register the converters
converter.resetSubconverters()
converter.registerSubconverter(ConverterBillboard)
converter.registerSubconverter(ConverterRollingStone)


if __name__ == '__main__':
    s = converter.parse(r'C:\Users\kaila\Desktop\meta-pop-corpus\sample_dataset\RS200\rs200_harmony\i_got_you_dt.har', format='rs', forceSource=True)
    s.show()
    s = converter.parse(r'C:\Users\kaila\Desktop\meta-pop-corpus\sample_dataset\McGill-BillBoard\SalamiFiles\1039.txt', format='billboard', forceSource=True)
    s.show('text')