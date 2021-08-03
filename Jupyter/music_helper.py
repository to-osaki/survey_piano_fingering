import music21 as mu

def key_pos(midi):
    d = [0, 0.5, 1, 1.5, 2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7]
    return midi // 12 * d[-1] + d[midi % 12]

def key_pos2(midi):
    x = key_pos(midi)
    y = 1 if x % 1 > 0 else 0
    return [x, y]

def note_pos(note):
    return key_pos(note.pitch.midi)

def note_pos2(note):
    return key_pos2(note.pitch.midi)

def note_color(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)