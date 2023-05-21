from PySide6.QtCore import QDir
from fileinfo import FileInfo
from filetags import FileTags
from exportParameters import ExportParameters
from filelist import FileList

if __name__ == "__main__":
    print("placeholderowy main")

    # Tworzenie obiektu klasy FileList
    file_list = FileList()

    # Dodawanie pojedynczego pliku
    file_list.addFile(QDir("/path/to/file.txt"))

    # Przeszukiwanie folderu i dodawanie plików
    file_list.searchFiles(QDir("/path/to/directory"))

    # Wyświetlanie listy plików
    file_list.printFiles()

    # Tworzenie obiektu klasy FileInfo
    file_info = FileInfo()

    # Wywołanie metody measureLoudness
    file_info.measureLoudness()

    # Tworzenie obiektu klasy FileTags
    file_tags1 = FileTags()
    file_tags1.tags = {"author": "John Doe", "year": 2023}

    # Tworzenie drugiego obiektu klasy FileTags
    file_tags2 = FileTags()
    file_tags2.tags = {"title": "My Document"}

    # Aktualizacja tagów pierwszego obiektu za pomocą drugiego obiektu
    file_tags1.updateTags(file_tags2)

    # Wyświetlanie tagów pierwszego obiektu
    print(file_tags1.tags)

    # Tworzenie obiektu klasy ExportParameters
    export_params = ExportParameters(format="MP3", bitrate="320kbps")

    # Wywołanie metody export
    file_info.export(export_params)
