import os
from PySide6.QtCore import QObject, QDir, QFile
from PySide6.QtWidgets import QWidget, QVBoxLayout
from fileinfo import FileInfo, FileInfoWidget


class FileList(QObject):
    files: list[FileInfoWidget] = []

    def addFile(self, directory, relative_path) -> FileInfoWidget:
        new_file = FileInfoWidget(self.parent(), directory, relative_path)
        self.files.append(new_file)
        return new_file

    def printFiles(self):
        for file in self.files:
            print(file.file_info)


class FileListWidget(QWidget):
    file_list: FileList

    def _addFileWidget(self, filepath, relative=""):
        widget = self.file_list.addFile(filepath, relative)
        self.widgets.addWidget(widget)

    def addFile(self, directory: QDir):
        for filename in directory.entryList():
            filepath = directory.filePath(filename)
            if QFile(filepath).isFile():
                self._addFileWidget(filepath)

    def addFolder(self, directory: QDir, recursive=False):
        if recursive:
            for root, dirs, files in directory.walk():
                for file in files:
                    filepath = directory.filePath(file)
                    self._addFileWidget(filepath, "")
        else:
            for filename in directory.entryList():
                filepath = directory.filePath(filename)
                if QFile(filepath).isFile():
                    self._addFileWidget(filepath, "")

    def __init__(self, parent):
        super().__init__(parent)
        self.file_list = FileList(self)
        self.widgets = QVBoxLayout()
