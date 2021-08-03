import pandas as pd
import re
import numpy as np
import music21 as mu
from music_helper import *

def read_PIG(path):
    """
    PIGデータセットの運指データをDataFrameとして読み出し
    """
    names = ["id", "t0", "t1", "note", "_n", "_v", "ch", "_finger"]
    table = pd.read_table(path, names = names, skiprows = 1)
    table["fingers"] = table["_finger"].apply(lambda s: [abs(int(n)) for n in str(s).split("_")])
    table["finger"] = table["fingers"].apply(lambda s: s[0])
    table["midi"] = table["note"].apply(lambda n: mu.note.Note(n).pitch.midi)
    table["pos"] = table["midi"].apply(lambda midi: key_pos(midi))
    return table

def read_fingering(path):
    """
    数値列のテキストをSeriesとして読み出し
    czernyR = read_fingering('./data/001-Czerny_fingering_R.txt')
    """
    with open(path) as f:
        st = f.read()
    return pd.Series([int(s) for s in re.split("", st) if s != "" and s != "_" and s != "\n"])

def convert_fingering_to_PIG(output_path, right_fingering_path, left_fingering_path, template_pig_path):
    """
    数値列のテキスト（左右手別）をPIGデータセットのフォーマットに変換
    convert_fingering_to_PIG(
        './data/001-Czerny_fingering.csv',
        './data/001-Czerny_fingering_R.txt', 
        './data/001-Czerny_fingering_L.txt', 
        './tmp/PianoFingeringDataset/FingeringFiles/001-1_fingering.txt')
    """
    rights = read_fingering(right_fingering_path)
    lefts = read_fingering(left_fingering_path)
    pig = read_PIG(template_pig_path)
    pig = pig.drop("finger", axis = 1)
    r = l = 0
    for i in range(len(pig)):
        ch = pig.iloc[i]["ch"]
        if ch == 1:
            pig.at[i, "_finger"] = "-" + str(lefts.at[l])
            l += 1
        else:
            pig.at[i, "_finger"] = str(rights.at[r])
            r += 1
    pig.to_csv(output_path, header=False, index=False, sep = "\t")
    return pig

def flength(time):
    """
    打鍵時間をquarterLengthに変換
    """
    threasholds = [0.099, 0.18, 0.34, 0.47, 0.60, 0.81, 1.00, 1.15, 1.30, 1.60, 1.75, 1.90, 2.00, 2.10, 2.20]
    lengths     = [0.125, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50, 2.75, 3.00, 3.25, 3.50]
    for i in range(len(threasholds)):
        if time < threasholds[i]:
            return lengths[i]
    return 4 # whole

def fnote(name, t):
    """
    音名と打鍵時間からmusic21.Noteを生成
    """
    return mu.note.Note(name=name, quarterLength=flength(t))

def appendPIGNotes(pig_notes, noteCallback = None):
    """
    PIGデータをmusic21.Noteに変換してStreamに追加
    """
    stream = mu.stream.Part()
    time = 0.0
    for i in range(len(pig_notes)):
        c = pig_notes.iloc[i]
        if(time < c.t0 and c.t0 - time > 1/32):
            r = mu.note.Rest(quarterLength=flength(c.t0 - time))
            stream.append(r)
        n = fnote(c.note, c.t1 - c.t0)
        if noteCallback is not None:
            noteCallback(i, n, c)
        stream.append(n)
        time = c.t1
    return stream

def makeScore(pig, title = "", composer = "", ts = "4/4"):
    """
    PIGデータを左右手２パートの楽譜に変換
    """
    score = mu.stream.Score()
    rights = pig[pig.ch == 0]
    if len(rights) > 0:
        pr = appendPIGNotes(rights, lambda i, n, c: n.addLyric(abs(int(str(c._finger).split("_")[0]))))
        pr.insert(0, mu.meter.TimeSignature(ts))
        score.insert(pr)
    lefts = pig[pig.ch == 1]
    if len(lefts) > 0:
        pl = appendPIGNotes(lefts, lambda i, n, c: n.addLyric(abs(int(str(c._finger).split("_")[0]))))
        pl.insert(0, mu.meter.TimeSignature(ts))
        score.insert(pl)
    if title is not None or composer is not None:
        score.insert(mu.metadata.Metadata())
        score.metadata.title = title
        score.metadata.composer = composer
    return score
