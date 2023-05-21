import os
from PySide6.QtCore import QObject, QDir
from PySide6.QtWidgets import QWidget
from fileinfo import FileInfo, FileInfoWidget


class FileList(QObject):
    files: list[FileInfoWidget] = []

    def addFile(self, directory: QDir):
        pass

    def addFolder(self, directory: QDir, recursive=False):
        pass

    def printFiles(self):
        for file in self.files:
            print(file.file_info)


class FileListWidget(QWidget):
    file_list: FileList

    def __init__(self, parent):
        super().__init__(parent)
        self.file_list = FileList(self)

