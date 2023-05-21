from PySide6.QtCore import QDir, QFile

class FileList:
    files = []

    def addFile(self, directory):
        assert QDir(directory).exists() and QDir(directory).isDir(), f"Directory '{directory}' does not exist or is not a directory."
        dir_obj = QDir(directory)
        for filename in dir_obj.entryList():
            filepath = dir_obj.filePath(filename)
            if QFile(filepath).isFile():
                self.files.append(filepath)

    def addFolder(self, directory, recursive=False):
        assert QDir(directory).exists() and QDir(directory).isDir(), f"Directory '{directory}' does not exist or is not a directory."
        dir_obj = QDir(directory)
        if recursive:
            for root, dirs, files in dir_obj.walk():
                for file in files:
                    filepath = dir_obj.filePath(file)
                    self.files.append(filepath)
        else:
            for filename in dir_obj.entryList():
                filepath = dir_obj.filePath(filename)
                if QFile(filepath).isFile():
                    self.files.append(filepath)

    def printFiles(self):
        for file in self.files:
            print(file)
