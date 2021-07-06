import pandas as pd
import re
import numpy as np
import music21 as mu

def read_PIG(path):
    """
    PIGデータセットの運指データをDataFrameとして読み出し
    """
    names = ["id", "t0", "t1", "note", "_n", "_v", "ch", "_finger"]
    table = pd.read_table(path, names = names, skiprows = 1)
    table["finger"] = table["_finger"].apply(lambda s: abs(int(str(s).split("_")[0])))
    return table

def read_fingering(path):
    """
    数値列のテキストをSeriesとして読み出し
    """
    with open(path) as f:
        st = f.read()
    return pd.Series([int(s) for s in re.split("", st) if s != "" and s != "_" and s != "\n"])

def convert_fingering_to_PIG(output_path, right_fingering_path, left_fingering_path, pig_path):
    """
    数値列のテキスト（左右手別）をPIGデータセットのフォーマットに変換
    """
    rights = read_fingering(right_fingering_path)
    lefts = read_fingering(left_fingering_path)
    pig = read_PIG(pig_path)
    pig = pig.drop("finger", axis = 1)
    r = l = 0
    for i in range(len(pig)):
        finger = pig.iloc[i]["_finger"]
        if finger.startswith("-"):
            pig.at[i, "_finger"] = "-" + str(lefts.at[l])
            l += 1
        else:
            pig.at[i, "_finger"] = str(rights.at[r])
            r += 1
    pig.to_csv(output_path, header=False, index=False, sep = "\t")

def flength(time):
    """
    打鍵時間をquarterLengthに変換
    """
    threasholds = [0.099, 0.18, 0.30, 0.47, 0.60, 0.81, 1.00, 1.15, 1.30, 1.60, 1.90]
    lengths     = [0.125, 0.25, 0.50, 0.75, 1.00, 1.25, 1.50, 1.75, 2.00, 2.25, 2.50]
    for i in range(len(threasholds)):
        if time < threasholds[i]:
            return lengths[i]
    return 4 # whole

def fnote(name, t):
    """
    音名と打鍵時間からmusic21.Noteを生成
    """
    return mu.note.Note(name=name, quarterLength=flength(t))

def appendPIGNotes(stream, pig_notes, noteCallback):
    """
    PIGデータをmusic21.Noteに変換してStreamに追加
    """
    time = 0.0
    for i in range(len(pig_notes)):
        c = pig_notes.iloc[i]
        if(time < c.t0 and c.t0 - time > 1/32):
            r = mu.note.Rest(quarterLength=flength(c.t0 - time))
            stream.append(r)
        n = fnote(c.note, c.t1 - c.t0)
        noteCallback(i, n, c)
        stream.append(n)
        time = c.t1