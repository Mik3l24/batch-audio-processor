import sys

from PySide6 import QtWidgets

from export_params import ExportParametersEditor
from filelist import FileListWidget
from tag_editor import FileTagsEditor


class MainWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.file_list_widget = FileListWidget(self)
        self.tags_widget = FileTagsEditor(self)
        self.params_widget = ExportParametersEditor(self)
        self.bar = ActionBar(self, self.file_list_widget)

        # Setup.
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.row1_layout = QtWidgets.QHBoxLayout(self)
        self.row2_layout = QtWidgets.QHBoxLayout(self)
        self.row3_layout = QtWidgets.QHBoxLayout(self)

        # Main layout.
        self.row1_layout.addWidget(self.bar.button_group)
        self.row2_layout.addWidget(self.file_list_widget.file_list_group)
        self.row2_layout.addWidget(self.tags_widget.tags_group)
        self.row3_layout.addWidget(self.params_widget.params)

        self.main_layout.addLayout(self.row1_layout)
        self.main_layout.addLayout(self.row2_layout)
        self.main_layout.addLayout(self.row3_layout)
        self.main_layout.layout().addStretch()


class ActionBar(QtWidgets.QWidget):
    def __init__(self, parent, flw: FileListWidget):
        super().__init__(parent)
        self.buttons_layout = QtWidgets.QHBoxLayout(self)
        self.button_group = QtWidgets.QGroupBox()

        self.button_open = QtWidgets.QPushButton("Otwórz plik")
        self.button_open_f = QtWidgets.QPushButton("Otwórz folder")
        self.button_delete = QtWidgets.QPushButton("Usuń zaznaczone z listy")
        self.button_check = QtWidgets.QPushButton("Zaznacz wszystko")
        self.button_uncheck = QtWidgets.QPushButton("Odznacz wszystko")
        self.button_vol_change = QtWidgets.QPushButton("Zmierz głośność")
        self.button_start = QtWidgets.QPushButton("Rozpocznij konwersję")

        self.buttons_layout.addWidget(self.button_open)
        self.buttons_layout.addWidget(self.button_open_f)
        self.buttons_layout.addWidget(self.button_delete)
        self.buttons_layout.addWidget(self.button_check)
        self.buttons_layout.addWidget(self.button_uncheck)
        self.buttons_layout.addWidget(self.button_vol_change)
        self.buttons_layout.addWidget(self.button_start)

        self.button_group.setLayout(self.buttons_layout)

        self.button_open.clicked.connect(lambda: self.open_file(flw))
        self.button_open_f.clicked.connect(lambda: self.open_folder(flw))
        self.button_delete.clicked.connect(lambda: FileListWidget.delete_files(flw))
        self.button_check.clicked.connect(lambda: FileListWidget.check_files(flw))
        self.button_uncheck.clicked.connect(lambda: FileListWidget.uncheck_files(flw))
        self.button_vol_change.clicked.connect(lambda: FileListWidget.mes_loud(flw))
        self.button_start.clicked.connect(lambda: FileListWidget.exp(flw))

    def open_file(self, flist: FileListWidget):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "Open file",
                                                         "", filter="Sound Files (*.wav *.ogg *.mp3 *.m4a)")
        flist.addFile(filename[0])

    def open_folder(self, flist: FileListWidget):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        # TODO Opcję rekursywnego dodawania plików.
        #  Najlepiej byłoby rozszerzyć QFileDialog o checkbox, ale osobny popup też może być.
        flist.addFolder(folder)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)
        self.setWindowTitle("Konwerter plików audio")
