import os


def deleteMp4(folderPath, changeName):
    files = os.listdir(folderPath)
    originFile = changeName + '.mp4'
    for file in files:
        if file != originFile:
            os.remove(os.path.join(folderPath, file))


def renameFile(path, oldname, changeName):
    os.rename(os.path.join(path, oldname), os.path.join(path, changeName))


def deleteM3u8(folderPath):
    files = os.listdir(folderPath)
    for file in files:
        if file.endswith('.m3u8'):
            os.remove(os.path.join(folderPath, file))
