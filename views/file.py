import os
from pathlib import Path

from PyQt5.QtCore import QDir, QFileInfo
from PyQt5.QtWidgets import QFileDialog, QFileSystemModel, QHBoxLayout, QLineEdit, QListView, QPushButton, QVBoxLayout, QWidget


class DirSelectFormView(QWidget):
    def __init__(self, *args, **kwargs):
        super(DirSelectFormView, self).__init__(*args, **kwargs)
        layout = QHBoxLayout(self)

        self.dirPathLineEdit = QLineEdit()
        self.dirPathLineEdit.setDisabled(True)
        self.dirSelectDialogBtn = QPushButton('Open')

        layout.addWidget(self.dirPathLineEdit)
        layout.addWidget(self.dirSelectDialogBtn)


class FileView(QWidget):
    def __init__(self, *args, **kwargs):
        super(FileView, self).__init__(*args, **kwargs)
        layout = QVBoxLayout(self)

        # Directory 선택 폼 설정
        self.dirSelectForm = DirSelectFormView()
        self.dirSelectForm.dirSelectDialogBtn.clicked.connect(self.openDirectorySelectDialog)
        layout.addWidget(self.dirSelectForm)

        # 파일 목록 화면 설정
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDot | QDir.AllDirs | QDir.Files)

        self.fileListView = QListView()
        self.fileListView.setModel(self.fileModel)
        self.fileListView.doubleClicked.connect(self.itemDoubleClicked)
        self.setDirectoryPath()
        layout.addWidget(self.fileListView)

    def setDirectoryPath(self, path=None):
        if path is None:
            path = os.path.join(os.path.expanduser('~'), 'Desktop')

        self.dirSelectForm.dirPathLineEdit.setText(path)

        rootIndex = self.fileModel.setRootPath(path)
        self.fileListView.setRootIndex(rootIndex)

    def openDirectorySelectDialog(self):
        rootPath = QFileDialog.getExistingDirectory(parent=self, caption="Select Directory", directory=self.dirSelectForm.dirPathLineEdit.text())

        if not rootPath:
            return

        self.setDirectoryPath(rootPath)

    def itemDoubleClicked(self, index):
        item: QFileInfo = self.fileModel.fileInfo(index)

        if item.isDir():
            dirPath = item.filePath()

            if dirPath.endswith('/..'):
                dirPath = '/'.join(dirPath.split('/')[:-2])

            self.setDirectoryPath(dirPath)