import sys

from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QHBoxLayout

from views.content import ContentView
from views.directory import DirectoryView
from views.file import FileView


class MainView(QWidget):
    def __init__(self, *args, **kwargs):
        super(MainView, self).__init__(*args, **kwargs)
        self.mainLayout = QHBoxLayout()

        self.fileView = FileView()
        self.contentView = ContentView()
        self.directoryView = DirectoryView()

        self.mainLayout.addWidget(self.fileView, stretch=2)
        self.mainLayout.addWidget(self.contentView, stretch=3)
        self.mainLayout.addWidget(self.directoryView, stretch=2)

        self.selectionModel = self.fileView.fileListView.selectionModel()
        self.selectionModel.selectionChanged.connect(self.selectionChanged)

        self.setWindowTitle('파일 분류기')
        self.setLayout(self.mainLayout)
        self.showMaximized()

    def selectionChanged(self, *args, **kwargs):
        selectedFileIndex = self.selectionModel.selection().indexes()[0]
        selectedFileInfo = self.fileView.fileModel.fileInfo(selectedFileIndex)

        self.contentView.showFile(selectedFileInfo)
        self.directoryView.setCurrentSelectedFile(selectedFileInfo)


app = QApplication(sys.argv)
ex = MainView()
sys.exit(app.exec_())
