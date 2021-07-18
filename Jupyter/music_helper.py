import music21 as mu

def key_pos(midi):
    d = [0, 0.5, 1, 1.5, 2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 7]
    return midi // 12 * d[-1] + d[midi % 12]

def note_pos(note):
    return key_pos(note.pitch.midi)

def note_dist(note1, note2):
    return key_pos(note2) - key_pos(note1)
