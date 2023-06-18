import os
from PySide6.QtCore import QObject, QDir, QFileInfo, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGroupBox, QLabel
from fileinfo import FileInfo, FileInfoWidget
from tag_editor import FileTagsEditor
from export_params import ExportParametersEditor, ExportParameters


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
            self.file_pressed()

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

    def delete_files(self):
        for index, file in enumerate(self.file_list.files):
            if file.is_checked:
                self.file_list.files.pop(index)
                self.file_list_layout.removeWidget(file)

    def check_files(self):
        for file in self.file_list.files:
            file.is_checked = True

    def uncheck_files(self):
        for file in self.file_list.files:
            file.is_checked = False

    def mes_loud(self):
        for file in self.file_list.files:
            if file.is_checked:
                FileInfo.measureLoudness(file.file_info)

    def exp(self, param):
        fp = ExportParameters(self)
        ExportParameters.setEncoder(fp, param.formatbox.currentText())
        for file in self.file_list.files:
            if file.is_checked:
                FileInfo.export(file.file_info, fp)

    def file_pressed(self):
        self.tags.titlebox.insert(self.file_list.files[0].file_info.desired_tags.tags['tracktitle'])
        self.tags.performerbox.insert(self.file_list.files[0].file_info.desired_tags.tags['artist'])
        self.tags.albumbox.insert(self.file_list.files[0].file_info.desired_tags.tags['album'])
        self.tags.dirbox.insert(self.file_list.files[0].file_info.relative_path)

    def __init__(self, parent, tags):
        super().__init__(parent)
        self.tags = tags
        self.file_list = FileList(self)

        self.file_list_layout = QVBoxLayout(self)
        self.file_list_group = QGroupBox(self)

        self.filelist_label = QLabel('Lista plików', self, alignment=Qt.AlignTop)

        self.file_list_layout.addWidget(self.filelist_label)

        self.file_list_group.setLayout(self.file_list_layout)
