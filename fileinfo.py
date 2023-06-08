import io
from typing import Optional

import scipy
from PySide6.QtCore import QObject, QDir, QFileInfo, SLOT
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

import pydub as pd
from pydub.silence import split_on_silence
import pyloudnorm as pyln
import numpy as np
import music_tag as tag

from filetags import FileTags
from export_params import ExportParameters, valid_extensions, DirOrg, Encoders


class FileInfo(QObject):
    absolute_path = ""
    relative_path = ""
    file_info: QFileInfo
    extension: str = ""
    original_tags: FileTags
    desired_tags: FileTags
    # Audio processing related
    loudness: Optional[float] = None
    sample_rate: Optional[int] = None
    _audio_segment: Optional[pd.AudioSegment] = None
    _audio_array: Optional[np.ndarray] = None

    def __init__(self, parent: "FileInfoWidget", absolute_path, relative_path):
        super().__init__(parent)
        self.absolute_path = absolute_path
        self.relative_path = relative_path
        self.file_info = QFileInfo(absolute_path)
        assert self.file_info.isFile() and self.file_info.completeSuffix() in valid_extensions
        self.extension = self.file_info.completeSuffix()
        self.original_tags = FileTags(tag.load_file(self.absolute_path))
        self.desired_tags = FileTags(tag.load_file(self.absolute_path))

    # Methods for loading audio data
    def loadAudioSegment(self):
        if self._audio_segment is None:
            self._audio_segment = pd.AudioSegment.from_file(self.absolute_path, self.extension)
            self.sample_rate = self._audio_segment.frame_rate

    def loadAudioArray(self):
        if self._audio_array is None:
            self.loadAudioSegment()
            data = np.array(self._audio_segment.get_array_of_samples())[::self._audio_segment.channels]
            data = data.astype(np.float32) / 10000
            data -= data.mean()
            self._audio_array = pyln.normalize.peak(data, -1.0)

    def arrayToSegment(self):
        # Convert back to AudioSegment
        wav_io = io.BytesIO()
        scipy.io.wavfile.write(wav_io, self.sample_rate, self._audio_array)
        wav_io.seek(0)
        self._audio_segment = pd.AudioSegment.from_wav(wav_io)

    def clearAudioData(self):
        self._audio_segment = None
        self._audio_array = None

    def measureLoudness(self):
        self.loadAudioArray()
        meter = pyln.Meter(self.sample_rate)
        self.loudness = meter.integrated_loudness(self._audio_array)

    def onlyMeasureLoudness(self) -> None:
        """
        Measure loudness and clear the loaded audio data
        """
        self.measureLoudness()
        self.clearAudioData()

    def normalizeLoudness(self, target_loudness: float = -23.0):
        self.measureLoudness()
        self._audio_array = pyln.normalize.loudness(self._audio_array, self.loudness, target_loudness)
        self.arrayToSegment()

    def cutSilence(self):
        self.loadAudioSegment()
        audio_chunks = split_on_silence(
            self._audio_segment,
            min_silence_len=2000,
            silence_thresh=-45,
            keep_silence=500, )
        self._audio_segment = sum(audio_chunks)

    def export(self, params: ExportParameters):
        # Load Data
        self.loadAudioSegment()
        # Normalize loudness
        if params.normalize_loudness and params.target_loudness is not None:
            self.normalizeLoudness(params.target_loudness)
        # Remove silence
        if params.cut_silence:
            self.cutSilence()
        # Get export destination
        dir = params.destination
        match params.organisation:
            case DirOrg.RELATIVE:
                dir += QDir.separator() + self.relative_path
            case DirOrg.TAGWISE:
                # Temporary, no parsing of tag pattern
                dir += QDir.separator() + self.desired_tags.tags["artist"] \
                       + QDir.separator() + self.desired_tags.tags["album"]
            # Default and SIMPLE case is absolute

        # Get extension
        self.extension = params.encoder.extension

        # Get export filename
        #   We forgot to add options for naming the file, so we'll just use the original filename
        filename = self.file_info.fileName()
        if QFileInfo(dir + QDir.separator() + filename).exists():
            # If the file already exists, we'll just add a number to the end
            i = 1
            temp_name = filename
            while QFileInfo(dir + QDir.separator() + temp_name + "." + self.extension).exists():
                temp_name = filename + f" ({i})"
                i += 1
            filename = temp_name
        dir += QDir.separator() + filename + "." + self.extension

        # Get export format
        match params.encoder:
            case Encoders.MP3():
                self._audio_segment.export(dir, format="mp3", bitrate=params.encoder.bitrate)
            case Encoders.WAV():
                self._audio_segment.export(dir, format="wav")
            case _:
                raise NotImplementedError("Unknown export format")

        # Set tags
        tag_file = tag.load_file(dir)
        for key, value in self.desired_tags.tags.items():
            tag_file[key] = value
        tag_file.save()

        self.clearAudioData()


class FileInfoWidget(QWidget):
    file_info: FileInfo
    selected: bool

    def __init__(self, parent, absolute_path, relative_path):
        super().__init__(parent)  # Parent is the FileListWidget or its layout
        self.file_info = FileInfo(self, absolute_path, relative_path)

        self.path_label = QLabel("cool")
        self.loudness_label = QLabel("")

        self.vlayout = QVBoxLayout(self)

        self.vlayout.addWidget(self.path_label)

        self.setLayout(self.vlayout)
        self.updateLabels()

    def updateLabels(self):
        self.path_label.setText(self.file_info.absolute_path)
        if self.file_info.loudness is None:
            self.loudness_label.setText(f"Not measured")
        else:
            self.loudness_label.setText(f"{self.file_info.loudness} LUFS")
