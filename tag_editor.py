from PySide6.QtWidgets import QWidget

from filetags import FileTags


class TagEditor(QWidget):
    tags: FileTags
