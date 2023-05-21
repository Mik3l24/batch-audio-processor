import os
from PySide6.QtCore import QDir

class FileList:
    files = []

    def addFile(self, directory):
        assert os.path.exists(directory) and directory.isDir(), f"Directory '{directory.path()}' does not exist or is not a directory."
        for filename in directory.entryList():
            filepath = directory.filePath(filename)
            if os.path.isfile(filepath):
                self.files.append(filepath)

    def addFolder(self, directory, recursive=False):
        assert directory.exists() and directory.isDir(), f"Directory '{directory.path()}' does not exist or is not a directory."
        if recursive:
            for root, dirs, files in os.walk(directory.path()):
                for file in files:
                    filepath = os.path.join(root, file)
                    self.files.append(filepath)
        else:
            for filename in directory.entryList():
                filepath = directory.filePath(filename)
                if os.path.isfile(filepath):
                    self.files.append(filepath)

    def printFiles(self):
        for file in self.files:
            print(file)
