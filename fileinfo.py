from PySide6.QtCore import QDir
from filetags import FileTags
from exportParameters import ExportParameters

class FileInfo:
    absolute_path: QDir
    relative_path: QDir
    original_tags: FileTags
    desired_tags: FileTags
    loudness: float

    def measureLoudness(self):
        # Implementacja funkcji measureLoudness
        print("Measuring loudness...")

    def export(self, export_params):
        if isinstance(export_params, ExportParameters):
            # Implementacja funkcji export
            print(f"Exporting file with parameters: {export_params}")
        else:
            print("Invalid input. Expected object of type ExportParameters.")
