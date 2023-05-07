# PRZED URUCHOMIENIEM ZAINSTALOWAC BIBLIOTEKE PYSIDE6 ORAZ NUMPY

from PySide6.QtCore import QDir

class FileTags:
    pass  # IMPLEMENTACJA KLASY FILETAGS


class ExportParameters: # EKSPORTOWANIE PARAMETROW DLA PYSIDE6 I NUMPY
    def __init__(self, requirements_file: str):
        with open(requirements_file, "r") as f:
            self.requirements = [line.strip() for line in f.readlines()]

    def get_requirements(self) -> list:
        return self.requirements


class FileInfo:
    def __init__(self, origin_path: QDir, relative_path: QDir, original_tags: FileTags, desired_tags: FileTags):
        self.origin_path = origin_path
        self.relative_path = relative_path
        self.original_tags = original_tags
        self.desired_tags = desired_tags
        self.loudness = None

    def measureLoudness(self):
        self.loudness = 0.0  # POMIAR GLOSNOSCI

    def export(self, parameters: ExportParameters):
        pass  # IMPLEMENTACJA METODY EXPORT

    def get_origin_path(self) -> QDir:
        return self.origin_path

    def get_relative_path(self) -> QDir:
        return self.relative_path

    def get_original_tags(self) -> FileTags:
        return self.original_tags

    def get_desired_tags(self) -> FileTags:
        return self.desired_tags

    def get_loudness(self) -> float:
        return self.loudness


class FileList:
    def __init__(self):
        self.files = []

    def addFile(self, file_path: QDir):
        file_info = FileInfo(file_path, QDir(), FileTags(), FileTags())
        self.files.append(file_info)

    def addFolder(self, folder_path: QDir, recursive: bool):
        if recursive:
            for file_path in folder_path.entryInfoList(QDir.Files | QDir.NoDotAndDotDot | QDir.Hidden | QDir.System):
                self.addFile(file_path)
            for subfolder_path in folder_path.entryInfoList(
                    QDir.Dirs | QDir.NoDotAndDotDot | QDir.Hidden | QDir.System):
                self.addFolder(subfolder_path, recursive=True)
        else:
            for file_path in folder_path.entryInfoList(QDir.Files | QDir.NoDotAndDotDot | QDir.Hidden | QDir.System):
                self.addFile(file_path)


if __name__ == "__main__":
    # PRZYKŁADOWE UŻYCIE KLAS
    file_list = FileList()
    file_list.addFolder(QDir("path/to/folder"), recursive=True)

    export_params = ExportParameters("requirements.txt")
    requirements = export_params.get_requirements()
    print(requirements)
