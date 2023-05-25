from enum import Enum
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
