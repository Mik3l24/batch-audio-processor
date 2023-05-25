import os
from PySide6.QtWidgets import QApplication
from filelist import FileList


def testLoading():
    filepath = os.path.dirname(os.path.abspath(__file__)) + "/audio-src/test.mp3"
    flist = FileList(None)
    try:
        flist.addFile(filepath, "")
    except AssertionError:
        print("Cool, not a file")
    else:
        print("Album: " + flist.files[0].file_info.original_tags.tags["album"])


if __name__ == "__main__":
    app = QApplication()
    testLoading()
