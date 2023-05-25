from typing import Optional
from PySide6.QtCore import QObject, QDir, QFileInfo
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
import pydub as pd
import music_tag as tag
from filetags import FileTags
from export_params import ExportParameters, valid_extensions


class FileInfo(QObject):
    absolute_path = ""
    relative_path = ""
    file_info: QFileInfo
    original_tags: FileTags
    desired_tags: FileTags
    loudness: Optional[float]

    def __init__(self, parent: "FileInfoWidget", absolute_path, relative_path):
        super().__init__(parent)
        self.absolute_path = absolute_path
        self.relative_path = relative_path
        self.file_info = QFileInfo(absolute_path)
        assert self.file_info.isFile() and self.file_info.completeSuffix() in valid_extensions.keys()

    def measureLoudness(self):
        # Implementacja funkcji measureLoudness
        print("Measuring loudness...")
        self.loudness = -12.0

    def export(self, export_params: ExportParameters):
        # Implementacja funkcji export
        print(f"Exporting file with parameters: {export_params}")


class FileInfoWidget(QWidget):
    file_info: FileInfo
    selected: bool

    def __init__(self, parent, absolute_path, relative_path):
        super().__init__(parent)  # Parent is the FileListWidget or its layout
        self.file_info = FileInfo(self, absolute_path, relative_path)

        self.path_label = QLabel("cool")
        self.loudness_label = QLabel

        self.vlayout = QVBoxLayout(self)

        self.vlayout.addWidget(self.path_label)

        self.setLayout(self.vlayout)
        self.updateLabels()

    def updateLabels(self):
        self.path_label.setText(self.file_info.absolute_path.absolutePath())
        self.loudness_label.setText(f"{self.file_info.loudness}")
