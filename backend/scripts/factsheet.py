from music21 import stream

def score_factsheet(score: stream.Score):
    factsheet = {}

    factsheet['tonic'] = score.keySignature.tonic.name
    factsheet['time_signature'] = score.timeSignature.ratioString if score.timeSignature else '?'
    
    sections = []
    chords = set()
    name = ''
    current_parent = score
    prev_lyric_count = 0
    progression = []
    song_progression = []
    for rn in score.recurse().notes:
        # a new formal section starts either when the note's immediate parent
        # stream changes (billboard-style scores: one Part per section) or
        # when it carries more lyrics than the previous note. music21's
        # Clercq-Temperley parser (rs format) labels the first note of each
        # section/reference expansion with an extra lyric holding its name,
        # even though the whole song ends up as a single flat stream with no
        # per-section Part to detect via activeSite alone.
        parent = rn.activeSite
        lyrics = [l.text for l in rn.lyrics]
        is_new_section = parent is not current_parent or len(lyrics) > prev_lyric_count
        if is_new_section:
            if progression:
                prog_string = '-'.join(progression)
                sections.append({'name': name, 'progression': prog_string})
            # setup new section
            name = lyrics[-1] if lyrics else (parent.id if parent is not None else '')
            progression = []
            # set stream parents
            current_parent = parent
        prev_lyric_count = len(lyrics)
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