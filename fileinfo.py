from typing import Optional
from PySide6.QtCore import QObject, QDir
from PySide6.QtWidgets import QWidget
from filetags import FileTags
from export_params import ExportParameters


class FileInfo(QObject):
    absolute_path: QDir
    relative_path: QDir
    original_tags: FileTags
    desired_tags: FileTags
    loudness: Optional[float]

    def __init__(self, parent: "FileInfoWidget", absolute_path: QDir, relative_path):
        super().__init__(parent)
        self.absolute_path = absolute_path
        self.relative_path = relative_path

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

    def __init__(self, parent, absolute_path: QDir, relative_path):
        super().__init__(parent)  # Parent is the FileListWidget or its layout
        self.file_info = FileInfo(self, absolute_path, relative_path)
