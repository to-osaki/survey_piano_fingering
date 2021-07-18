import os.path

def getFilename(path):
    return os.path.splitext(os.path.basename(path))[0]