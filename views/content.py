from dataclasses import dataclass

from PyQt5.QtCore import QFileInfo, QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileIconProvider, QLabel, QVBoxLayout, QWidget


@dataclass
class File:
    fileInfo: 'QFileInfo'

    @property
    def name(self):
        return self.fileInfo.fileName()

    @property
    def path(self):
        return self.fileInfo.filePath()

    @property
    def size(self):
        return self.fileInfo.size()

    @property
    def ext(self):
        return self.fileInfo.suffix().lower()


class ContentView(QWidget):
    def __init__(self):
        super().__init__()

        self.selectedFile = None

        self.mainLayout = QVBoxLayout()

        # creating label
        self.imageLabel = QLabel(self)
        self.imageLabel.setText('no file')
        self.imageLabel.setScaledContents(True)
        self.imageLabel.resize(self.width(), self.height())

        self.setLayout(self.mainLayout)

    def showFile(self, fileInfo: 'QFileInfo'):
        def isImageFile(file: File):
            return file.ext in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif']

        self.selectedFile = File(fileInfo)

        if isImageFile(self.selectedFile):
            pixmap = QPixmap(self.selectedFile.path)
        else:
            icon = QFileIconProvider().icon(fileInfo)
            pixmap = icon.pixmap(self.width(), self.height())

        self.imageLabel.setPixmap(pixmap.scaled(self.width(), self.height(), Qt.KeepAspectRatio))

    def resetFile(self):
        self.selectedFile = None
        self.imageLabel.setText('no file')
