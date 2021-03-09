from PyQt5.QtCore import QFileInfo
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ContentView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        # creating label
        self.imageLabel = QLabel(self)
        self.imageLabel.setText('image')

        self.setLayout(self.mainLayout)

    def showFile(self, fileInfo: 'QFileInfo'):
        pixmap = QPixmap(fileInfo.filePath())

        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.resize(self.width(), self.height())
