from fileinfo import file_info

class ExportParameters:
    def __init__(self, format, bitrate):
        self.format = format
        self.bitrate = bitrate

    def __str__(self):
        return f"Format: {self.format}, Bitrate: {self.bitrate}"

