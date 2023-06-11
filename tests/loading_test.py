import os
from math import isclose
from PySide6.QtWidgets import QApplication

from export_params import ExportParameters, Encoders, DirOrg
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
    assert file.loudness is None
    file.measureLoudness()
    print(file.loudness)
    assert file.loudness is not None
    file.normalizeLoudness(-21)
    file.measureLoudness()
    assert isclose(file.loudness, -21, abs_tol=0.5)
    print(file.loudness)


def testExport():
    widget = FileInfoWidget(None, os.getcwd()+"/audio-src/test.mp3", "")
    file = widget.file_info
    # Change tags
    file.desired_tags.tags["title"] = "cool song"
    file.desired_tags.tags["artist"] = "artist"
    file.desired_tags.tags["album"] = "album"
    file.desired_tags.tags["comment"] = "testing testing"
    # Prepare export parameters
    params = ExportParameters(None)
    params.destination = os.getcwd()+"/audio-dest"
    params.encoder = Encoders.MP3()
    params.organisation = DirOrg.TAGWISE
    params.target_loudness = -21
    params.normalize_loudness = True
    params.cut_silence = False  # too slow
    # Export
    file.export(params)
    # Test that the file exists
    assert os.path.isfile(params.destination + "/artist/album/test.mp3")

    # TODO apparently it exports to mono


if __name__ == "__main__":
    app = QApplication()
    testLoading()
    testNormalization()
    testExport()
