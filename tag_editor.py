from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QWidget

from filetags import FileTags


class FileTagsEditor(QtWidgets.QWidget):
    tags: FileTags

    def __init__(self, parent):
        super().__init__(parent)
        self.tags_layout = QtWidgets.QVBoxLayout(self)
        self.tags_group = QtWidgets.QGroupBox()

        self.intags_layout1 = QtWidgets.QHBoxLayout(self)
        self.intags_layout2 = QtWidgets.QHBoxLayout(self)
        self.intags_layout3 = QtWidgets.QHBoxLayout(self)
        self.intags_layout4 = QtWidgets.QHBoxLayout(self)
        self.intags_layout5 = QtWidgets.QHBoxLayout(self)

        self.tags_label = QtWidgets.QLabel("Tagi pliku", self, alignment=QtCore.Qt.AlignTop)

        self.tags_layout.addWidget(self.tags_label)

        # TODO Generuj opcje do tagów programowo, dla każdego tagu w dict
        self.title_label = QtWidgets.QLabel("Tytuł: ")
        self.titlebox = QtWidgets.QLineEdit(self)
        self.intags_layout1.addWidget(self.title_label)
        self.intags_layout1.addWidget(self.titlebox)

        self.performer_label = QtWidgets.QLabel("Wykonawca: ")
        self.performerbox = QtWidgets.QLineEdit(self)
        self.intags_layout2.addWidget(self.performer_label)
        self.intags_layout2.addWidget(self.performerbox)

        self.album_label = QtWidgets.QLabel("Album: ")
        self.albumbox = QtWidgets.QLineEdit(self)
        self.intags_layout3.addWidget(self.album_label)
        self.intags_layout3.addWidget(self.albumbox)

        self.dir_label = QtWidgets.QLabel("Ścieżka względna: ")
        self.dirbox = QtWidgets.QLineEdit(self)
        self.intags_layout4.addWidget(self.dir_label)
        self.intags_layout4.addWidget(self.dirbox)

        # To akurat jest w porządku
        self.button_a = QtWidgets.QPushButton("Zatwierdź tagi")
        self.button_b = QtWidgets.QPushButton("Przywróć domyślne")
        self.intags_layout5.addWidget(self.button_a)
        self.intags_layout5.addWidget(self.button_b)

        self.button_a.clicked.connect(lambda: FileTags.updateTags(self.tags, self.tags))
        self.button_b.clicked.connect(lambda: FileListWidget.file_pressed())

        self.tags_layout.addLayout(self.intags_layout1)
        self.tags_layout.addLayout(self.intags_layout2)
        self.tags_layout.addLayout(self.intags_layout3)
        self.tags_layout.addLayout(self.intags_layout4)
        self.tags_layout.addLayout(self.intags_layout5)

        self.tags_group.setLayout(self.tags_layout)
