import os
import shutil

from PyQt5.QtCore import QFileInfo, QModelIndex
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QListView, QVBoxLayout, QWidget


class DirectoryView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.selectedFileInfo = None

        self.directoryListModel = QStandardItemModel()
        self.directoryListView = QListView()
        self.directoryListView.clicked.connect(self.selectDirectory)
        self.directoryListView.setModel(self.directoryListModel)

        for path in os.listdir('/Users/kyungseokpark/Desktop/test'):
            item = QStandardItem(os.path.join('/Users/kyungseokpark/Desktop/test', path))
            self.directoryListModel.appendRow(item)

        self.mainLayout.addWidget(self.directoryListView)
        self.setLayout(self.mainLayout)

    def setCurrentSelectedFile(self, fileInfo: 'QFileInfo'):
        self.selectedFileInfo = fileInfo

    def selectDirectory(self, index: 'QModelIndex'):
        data = self.directoryListModel.data(index)
        print(data)

        if self.selectedFileInfo is not None and self.selectedFileInfo.isFile():
            print(f'move {self.selectedFileInfo.filePath()} to {data}')
            # os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
            shutil.move(self.selectedFileInfo.filePath(), data)
            # os.replace("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
