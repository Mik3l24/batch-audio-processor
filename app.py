import sys
from PySide6 import QtCore, QtWidgets
from pathlib import PurePath
from filelist import FileList


# from PySide6.QtWidgets import QMainWindow
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         #self.setCentralWidget()


class App(QtWidgets.QWidget):
    def __init__(self, bw, flw, fl, tw, pw):
        super().__init__()
        # Setup.
        self.main_layout = QtWidgets.QVBoxLayout(self)

        self.row1_layout = QtWidgets.QHBoxLayout(self)
        self.row2_layout = QtWidgets.QHBoxLayout(self)
        self.row3_layout = QtWidgets.QHBoxLayout(self)

        # Main layout.
        self.row1_layout.addWidget(bw.button_group)
        self.row2_layout.addWidget(flw.filelist)
        self.row2_layout.addWidget(tw.tags)
        self.row3_layout.addWidget(pw.params)

        self.main_layout.addLayout(self.row1_layout)
        self.main_layout.addLayout(self.row2_layout)
        self.main_layout.addLayout(self.row3_layout)
        self.main_layout.layout().addStretch()

    # def list_add(self, flist):
    #     for file in flist:
    #         self.filelist_layout.addWidget(self.make_widget(file))
    #         self.filelist.setLayout(self.filelist_layout)
    #
    # def make_widget(self, file):
    #     filename = PurePath(file).name
    #     filepath = file
    #     filespath = PurePath(file).parent.parts[-1]
    #     loudness = 'loudness: -12'
    #     fileinfo = filename + '\n' + filepath + '\n' + filespath + '\n' + loudness
    #     file_text = QtWidgets.QLabel(fileinfo, alignment=QtCore.Qt.AlignLeft)
    #     # file_text.mousePressEvent()
    #     return file_text


class ButtonsWidget(QtWidgets.QWidget):
    def __init__(self, fl):
        super().__init__()
        self.buttons_layout = QtWidgets.QHBoxLayout(self)
        self.button_group = QtWidgets.QGroupBox()

        self.button_open = QtWidgets.QPushButton('Otwórz plik')
        self.button_open_f = QtWidgets.QPushButton('Otwórz folder')
        self.button_delete = QtWidgets.QPushButton('Usuń zaznaczone z listy')
        self.button_check = QtWidgets.QPushButton('Zaznacz wszystko')
        self.button_uncheck = QtWidgets.QPushButton('Odznacz wszystko')
        self.button_vol_change = QtWidgets.QPushButton('Zmierz głośność')
        self.button_start = QtWidgets.QPushButton('Rozpocznij konwersję')

        self.buttons_layout.addWidget(self.button_open)
        self.buttons_layout.addWidget(self.button_open_f)
        self.buttons_layout.addWidget(self.button_delete)
        self.buttons_layout.addWidget(self.button_check)
        self.buttons_layout.addWidget(self.button_uncheck)
        self.buttons_layout.addWidget(self.button_vol_change)
        self.buttons_layout.addWidget(self.button_start)

        self.button_group.setLayout(self.buttons_layout)

        self.button_open.clicked.connect(lambda: self.open_file(fl))
        self.button_open_f.clicked.connect(lambda: self.open_folder(fl))

    def open_file(self, flist):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file',
                                                         '', 'Sound Files (*.wav *.ogg *.mp3 *.m4a)')
        flist.addFile(QtCore.QDir(filename[0]))

    def open_folder(self, flist):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Directory')
        flist.addFolder(QtCore.QDir(folder[0]))


class FileListWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.filelist_layout = QtWidgets.QVBoxLayout(self)
        self.filelist = QtWidgets.QGroupBox()

        self.filelist_label = QtWidgets.QLabel('Lista plików', alignment=QtCore.Qt.AlignTop)

        self.filelist_layout.addWidget(self.filelist_label)

        self.filelist.setLayout(self.filelist_layout)


class FileTagsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.tags_layout = QtWidgets.QVBoxLayout(self)
        self.tags = QtWidgets.QGroupBox()

        self.intags_layout1 = QtWidgets.QHBoxLayout(self)
        self.intags_layout2 = QtWidgets.QHBoxLayout(self)
        self.intags_layout3 = QtWidgets.QHBoxLayout(self)
        self.intags_layout4 = QtWidgets.QHBoxLayout(self)
        self.intags_layout5 = QtWidgets.QHBoxLayout(self)

        self.tags_label = QtWidgets.QLabel('Tagi pliku', alignment=QtCore.Qt.AlignTop)

        self.tags_layout.addWidget(self.tags_label)

        self.title_label = QtWidgets.QLabel('Tytuł: ')
        self.titlebox = QtWidgets.QLineEdit(self)
        self.intags_layout1.addWidget(self.title_label)
        self.intags_layout1.addWidget(self.titlebox)

        self.performer_label = QtWidgets.QLabel('Wykonawca: ')
        self.performerbox = QtWidgets.QLineEdit(self)
        self.intags_layout2.addWidget(self.performer_label)
        self.intags_layout2.addWidget(self.performerbox)

        self.album_label = QtWidgets.QLabel('Album: ')
        self.albumbox = QtWidgets.QLineEdit(self)
        self.intags_layout3.addWidget(self.album_label)
        self.intags_layout3.addWidget(self.albumbox)

        self.dir_label = QtWidgets.QLabel('Ścieżka względna: ')
        self.dirbox = QtWidgets.QLineEdit(self)
        self.intags_layout4.addWidget(self.dir_label)
        self.intags_layout4.addWidget(self.dirbox)

        self.button_a = QtWidgets.QPushButton('Zatwierdź tagi')
        self.button_b = QtWidgets.QPushButton('Przywróć domyślne')
        self.intags_layout5.addWidget(self.button_a)
        self.intags_layout5.addWidget(self.button_b)

        self.tags_layout.addLayout(self.intags_layout1)
        self.tags_layout.addLayout(self.intags_layout2)
        self.tags_layout.addLayout(self.intags_layout3)
        self.tags_layout.addLayout(self.intags_layout4)
        self.tags_layout.addLayout(self.intags_layout5)

        self.tags.setLayout(self.tags_layout)


class ParamsWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.params_layout = QtWidgets.QVBoxLayout(self)
        self.params = QtWidgets.QGroupBox()

        self.params_label = QtWidgets.QLabel('Parametry eksportu', alignment=QtCore.Qt.AlignHCenter)

        self.params_layout.addWidget(self.params_label)

        self.inparams1_layout1 = QtWidgets.QHBoxLayout(self)
        self.inparams1_layout2 = QtWidgets.QHBoxLayout(self)
        self.inparams1_layout3 = QtWidgets.QHBoxLayout(self)

        self.params2_label = QtWidgets.QLabel('Lokalizacja, organizacja eksportowanych plików',
                                              alignment=QtCore.Qt.AlignHCenter)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    filelist = FileList()
    buttons_widget = ButtonsWidget(filelist)
    filelist_widget = FileListWidget()
    tags_widget = FileTagsWidget()
    params_widget = ParamsWidget()

    widget = App(buttons_widget, filelist_widget, filelist, tags_widget, params_widget)
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
