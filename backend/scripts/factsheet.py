from music21 import stream

def score_factsheet(score: stream.Score):
    factsheet = {}

    factsheet['tonic'] = score.keySignature.tonic.name
    factsheet['time_signature'] = score.timeSignature.ratioString if score.timeSignature else '?'
    
    sections = []
    chords = set()
    name = ''
    current_parent = score
    progression = []
    song_progression = []
    for rn in score.recurse().notes:
        # get parent stream
        parent = rn.activeSite
        # start new section if different parent from last note
        if parent is not current_parent:
            if progression:
                prog_string = '-'.join(progression)
                sections.append({'name': name, 'offset': current_parent.offset, 'progression': prog_string})
            # setup new section
            name = parent.id
            progression = []
            # set stream parents
            current_parent = parent
        numeral = rn.romanNumeral.replace('-', 'b')
        # add note to the progression if different from last
        if not progression or progression[-1] != numeral:
            progression.append(numeral)
            chords.add(numeral)
        if not song_progression or song_progression[-1] != numeral:
            song_progression.append(numeral) 
    # append final section
    if progression:
        prog_string = '-'.join(progression)
        sections.append({'name': name, 'progression': prog_string})

    factsheet['chords'] = list(chords)
    factsheet['structure'] = [section['name'] for section in sections]
    factsheet['sections'] = sections
    factsheet['progression'] = '-'.join(song_progression)

    return factsheet