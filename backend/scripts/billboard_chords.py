from music21 import chord, duration, harmony, pitch

CHORD_SHORTHANDS = {
    '1': (),
    'maj': ('3', '5'),
    'min': ('b3', '5'),
    'dim': ('b3', 'b5'),
    'aug': ('3', '#5'),
    '5': ('5',),
    'maj7': ('3', '5', '7'),
    'min7': ('b3', '5', 'b7'),
    '7': ('3', '5', 'b7'),
    'dim7': ('b3', 'b5', 'bb7'),
    'hdim7': ('b3', 'b5', 'b7'),
    'minmaj7': ('b3', '5', '7'),
    'maj6': ('3', '5', '6'),
    'min6': ('b3', '5', '6'),
    '9': ('3', '5', 'b7', '9'),
    'maj9': ('3', '5', '7', '9'),
    'min9': ('b3', '5', 'b7', '9'),
    '11': ('3', '5', 'b7', '9', '11'),
    'maj11': ('3', '5', '7', '9', '11'),
    'min11': ('b3', '5', 'b7', '9', '11'),
    '13': ('3', '5', 'b7', '9', '11', '13'),
    'maj13': ('3', '5', '7', '9', '11', '13'),
    'min13': ('b3', '5', 'b7', '9', '11', '13'),
    'sus2': ('2', '5'),
    'sus4': ('4', '5'),
}

# initialise programatically
COMPONENT_INTERVALS = {}
for i in range(14):
    if i % 7 in (1, 4, 5):
        COMPONENT_INTERVALS[f'b{i}'] = f'd{i}'
        COMPONENT_INTERVALS[f'{i}'] = f'P{i}'
        COMPONENT_INTERVALS[f'#{i}'] = f'A{i}'
    else:
        COMPONENT_INTERVALS[f'bb{i}'] = f'd{i}'
        COMPONENT_INTERVALS[f'b{i}'] = f'm{i}'
        COMPONENT_INTERVALS[f'{i}'] = f'M{i}'
        COMPONENT_INTERVALS[f'#{i}'] = f'A{i}'

def billboard_chord(string: str, qtr_len = None) -> chord.Chord:
    root, details = string.split(':')
    root = root.replace('b', '-')
    type = None
    bass = None
    degrees = set()
    if '/' in details:
        details, bass = details.split('/')
        degrees |= {bass}
    if '(' in details and ')' in details:
        type, details = details.split('(')
        degrees |= set(CHORD_SHORTHANDS[type])
        mods = details.split(')')[0].split(',')
        for mod in mods:
            if mod[0] == '*':
                degrees.discard(mod[1:])
            else:
                degrees.add(mod)
    else:
        type = details
        degrees |= set(CHORD_SHORTHANDS[type])
    root = pitch.Pitch(f'{root}4')
    degrees = [root.transpose(COMPONENT_INTERVALS[deg]) for deg in degrees]
    #print(degrees)
    c = chord.Chord([root] + degrees)
    #print(c)
    if qtr_len: c.duration = duration.Duration(qtr_len)
    if bass:
        bass = abs(int(bass.replace('b', '').replace('#', '')))
        if bass % 2 == 1:
            inversion = (bass - 1) // 2
            if inversion < len(c.pitches): 
                c.inversion(inversion)
    annotation = string.replace(':', '')
    # add any additional annotation changes
    c.lyric = annotation
    return c