from enum import Enum

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QObject, QDir
from PySide6.QtWidgets import QWidget


# Directory Organisation on export
class DirOrg(Enum):
    SIMPLE = 0
    RELATIVE = 1
    TAGWISE = 3


valid_extensions = [
    "mp3",
    "wav",
    "ogg",
]


class Encoders:
    class Encoder:
        pass

    class MP3(Encoder):
        bitrate = 320

    class WAV(Encoder):
        bit_depth = 16


_available_encoders = {
    "MP3": Encoders.MP3(),
    "WAV": Encoders.WAV(),
}


class ExportParameters(QObject):
    destination: QDir
    organisation: DirOrg = DirOrg.SIMPLE
    tag_pattern: str = ""
    encoder: Encoders.Encoder

    def __init__(self, parent):
        super().__init__(parent)

    def setEncoder(self, type: str):
        assert type in _available_encoders.keys()
        self.encoder = _available_encoders[type]

    def __str__(self):
        return f"Destination: {self.destination}, Organisation: {self.organisation}"


class ExportParametersEditor(QWidget):
    export_params: ExportParameters

    def __init__(self, parent):
        super().__init__(parent)
        self.export_params = ExportParameters(self)

        self.params_layout = QtWidgets.QVBoxLayout(self)
        self.params = QtWidgets.QGroupBox()

        self.params_label = QtWidgets.QLabel('Parametry eksportu', self, alignment=QtCore.Qt.AlignHCenter)

        self.params_layout.addWidget(self.params_label)

        self.inparams1_layout1 = QtWidgets.QHBoxLayout(self)
        self.inparams1_layout2 = QtWidgets.QHBoxLayout(self)
        self.inparams1_layout3 = QtWidgets.QHBoxLayout(self)

        self.params2_label = QtWidgets.QLabel('Lokalizacja, organizacja eksportowanych plików',
                                              self, alignment=QtCore.Qt.AlignHCenter)
        self.inparams1_layout1.addWidget(self.params2_label)

        self.folder_label = QtWidgets.QLabel('Folder docelowy: ')
        self.folderbox = QtWidgets.QLineEdit(self)
        self.inparams1_layout2.addWidget(self.folder_label)
        self.inparams1_layout2.addWidget(self.folderbox)

        self.radio1 = QtWidgets.QRadioButton('zachowaj ścieżkę względną')
        self.radio1.setChecked(True)
        self.radio2 = QtWidgets.QRadioButton('wszystko do tego samego folderu')
        self.radio3 = QtWidgets.QRadioButton('wg. tagów')

        self.bytbox = QtWidgets.QLineEdit(self)

        self.inparams1_layout3.addWidget(self.radio1)
        self.inparams1_layout3.addWidget(self.radio2)
        self.inparams1_layout3.addWidget(self.radio3)
        self.inparams1_layout3.addWidget(self.bytbox)

        self.params_layout.addLayout(self.inparams1_layout1)
        self.params_layout.addLayout(self.inparams1_layout2)
        self.params_layout.addLayout(self.inparams1_layout3)

        self.inparams2_layout = QtWidgets.QHBoxLayout(self)

        self.format_label = QtWidgets.QLabel('Format: ')
        self.formatbox = QtWidgets.QLineEdit(self)
        self.inparams2_layout.addWidget(self.format_label)
        self.inparams2_layout.addWidget(self.formatbox)

        self.params_layout.addLayout(self.inparams2_layout)

        self.inparams3_layout = QtWidgets.QHBoxLayout(self)

        self.sound_label = QtWidgets.QLabel('Głośność docelowa: ')
        self.soundbox = QtWidgets.QLineEdit(self)
        self.check1 = QtWidgets.QCheckBox('Usuń ciszę')
        self.check1.setChecked(True)
        self.inparams3_layout.addWidget(self.sound_label)
        self.inparams3_layout.addWidget(self.soundbox)
        self.inparams3_layout.addWidget(self.check1)

        self.params_layout.addLayout(self.inparams3_layout)

        self.params.setLayout(self.params_layout)

