from music21 import stream, key, chord, roman, scale

def estimate_jp_key(score: stream.Score):
    # find major key yielding least accidentals and convert
    mKey = key.Key('C')
    pitches = {}
    # tally the total instances of each pitch
    for note in score.recurse().notes:
        for pitch in note.pitches:
            name = pitch.name
            if name in pitches:
                pitches[name] += 1
            else:
                pitches[name] = 1
    # find the both common form of each note
    seven_tally = {p: 0 for p in 'ABCDEFG'}
    seven_pitches = {p: None for p in 'ABCDEFG'}
    for pitch in 'ABCDEFG':
        for mod in (pitch + '-', pitch, pitch + '#'):
            if mod in pitches and pitches[mod] > seven_tally[pitch]:
                seven_pitches[pitch] = mod
                seven_tally[pitch] = pitches[mod]
    final_pitches = {p for p in seven_pitches.values() if p}
    # for each pitch see if major key matches most common pitches
    for pitch in final_pitches:
        pitch_set = {p.name for p in scale.MajorScale(pitch).pitches}
        if final_pitches.issubset(pitch_set):
            mKey = key.Key(pitch)
            #print(mKey)
            break

    return mKey


def convert_to_jp_key(old_stream: stream.Stream, new_key=None):
    if new_key == None:
        new_key = estimate_jp_key(old_stream)

    new_stream = type(old_stream)()
    new_stream.id = old_stream.id
    for el in old_stream:
        offset = el.offset
        # use recursion to convert streams
        if isinstance(el, stream.Stream):
            new_stream.insert(offset, convert_to_jp_key(el, new_key))
        # convert all chord elements to roman numerals
        elif isinstance(el, chord.Chord):
            rn = roman.romanNumeralFromChord(el, new_key)
            rn.quarterLength = el.quarterLength
            rn.addLyric(rn.figure)
            for l in el.lyrics:
                rn.addLyric(l.text)
            new_stream.insert(offset, rn)
        # convert all key signatures to new key
        elif isinstance(el, key.KeySignature):
            new_stream.insert(offset, key.Key(*new_key.name.split()))
        # insert all other elements
        else:
            new_stream.insert(offset, el)
            
    return new_stream