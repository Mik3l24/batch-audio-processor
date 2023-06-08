import os
from PySide6.QtWidgets import QApplication
from filelist import FileList
from fileinfo import FileInfo, FileInfoWidget

def testLoading():
    filepath = os.path.dirname(os.path.abspath(__file__)) + "/audio-src/test.mp3"
    flist = FileList(None)
    try:
        flist.addFile(filepath, "")
    except AssertionError:
        print("Cool, not a file")
    else:
        print("Album: " + flist.files[0].file_info.original_tags.tags["album"])


def testNormalization():
    widget = FileInfoWidget(None, os.getcwd()+"/audio-src/test.mp3", "")
    file = widget.file_info
    print(file.loudness)
    file.measureLoudness()
    print(file.loudness)
    file.normalizeLoudness(-21)
    file.measureLoudness()
    print(file.loudness)


if __name__ == "__main__":
    app = QApplication()
    testLoading()
    testNormalization()
