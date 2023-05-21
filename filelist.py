import os
from PySide6.QtCore import QObject, QDir
from PySide6.QtWidgets import QWidget
from fileinfo import FileInfo, FileInfoWidget


class FileList(QObject):
    files: list[FileInfoWidget] = []

    def addFile(self, directory: QDir, relative_path) -> FileInfoWidget:
        new_file = FileInfoWidget(self.parent(), directory, relative_path)
        self.files.append(new_file)
        return new_file

    def printFiles(self):
        for file in self.files:
            print(file.file_info)


class FileListWidget(QWidget):
    file_list: FileList

    def addFile(self, directory: QDir, relative_path):
        widget = self.file_list.addFile(directory, relative_path)
        self.widgets.addWidget(widget)

    def addFolder(self, directory: QDir, recursive=False):
        pass  # Call addFile

    def __init__(self, parent):
        super().__init__(parent)
        self.file_list = FileList(self)


