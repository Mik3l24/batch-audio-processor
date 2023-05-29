import os
from PySide6.QtCore import QObject, QDir, QFileInfo, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel
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
        if QFileInfo(filepath).isFile():
            widget = self.file_list.addFile(filepath, relative)
            self.file_list_layout.addWidget(widget)

    def addFile(self, path):
        self._addFileWidget(path)

    def addFolder(self, path, recursive=False):
        qdir = QDir(path)
        if recursive:
            for root, dirs, files in qdir.walk():
                for file in files:
                    filepath = qdir.filePath(file)
                    self._addFileWidget(filepath, "")
        else:
            for filename in qdir.entryList():
                filepath = qdir.filePath(filename)
                self._addFileWidget(filepath, "")

    def __init__(self, parent):
        super().__init__(parent)
        self.file_list = FileList(self)

        self.file_list_layout = QVBoxLayout(self)
        self.file_list_group = QGroupBox(self)

        self.filelist_label = QLabel('Lista plików', self, alignment=Qt.AlignTop)

        self.file_list_layout.addWidget(self.filelist_label)

        self.file_list_group.setLayout(self.file_list_layout)
        

