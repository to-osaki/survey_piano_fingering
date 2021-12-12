import music21 as mu
import numpy as np

# 88鍵　A0～C8 (21～108) を、X位置(黒鍵は0.5として１オクターブ=7)に変換
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

def note_gray(g):
    return "#{:02x}{:02x}{:02x}".format(g, g, g)

# return ["寄せ", "拡げ", "潜り", "超え", "その他"]
def getMoveTypeByPIGNote(n, n_, ignoreChords):
    if ignoreChords and abs(n.t0 - n_.t0) < 0.01:
        return 4
    return getMoveType(n.fingers, n_.fingers, n.pos, n_.pos)

def getMoveType(fingers, fingers_prev, pos, pos_prev):
    fng = fingers[0]
    fng_prev = fingers_prev[-1]
    ch = 0 if fng > 0 else -1
    sign = 1 if ch == 0 else -1
    pd_ = (pos - pos_prev) * sign
    fd_ = (fng - fng_prev) * sign
    move = 4
    thumb = abs(fng) == 1 or abs(fng_prev) == 1
    # 替え指
    if len(fingers) > 1:
        move = 0
    # 鍵盤上の距離より、指番号の差の方が大きい＝指寄せ
    elif np.sign(pd_) == np.sign(fd_) and abs(pd_) < abs(fd_) - 0.5:
        move = 0
    # 鍵盤上の距離より、指番号の差の方が小さい=拡げ
    elif np.sign(pd_) == np.sign(fd_) and abs(pd_) > abs(fd_) + (1.5 if thumb else 0.5):
        # if abs(fng) != 1 and abs(fng_prev) != 1 and abs(fng) != 5 and abs(fng_prev) != 5:
        # if pd < (6 if thumb else 5)
            move = 1
    # 指くぐり、指超え
    elif np.sign(pd_) != np.sign(fd_):
        if fd_ == 0:
            move = 1
        elif np.sign(pd_) >= 0 and abs(fng) == 1:
            move = 2
        elif np.sign(pd_) <= 0 and abs(fng_prev) == 1:
            move = 3
        else:
            move = 0
    return move