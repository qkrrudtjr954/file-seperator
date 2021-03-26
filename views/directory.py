import os
import shutil

from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QVBoxLayout, QWidget


class DirSelectFormView(QWidget):
    def __init__(self, *args, **kwargs):
        super(DirSelectFormView, self).__init__(*args, **kwargs)
        self.mainLayout = QHBoxLayout(self)
        self.dirSelectDialogBtn = QPushButton('+ add folder')
        self.mainLayout.addWidget(self.dirSelectDialogBtn)


class DirectoryItem(QWidget):
    def __init__(self, parent=None):
        super(DirectoryItem, self).__init__(parent=parent)
        self.mainLayout = QHBoxLayout()

        self.iconQLabel = QLabel(self)
        self.iconQLabel.setPixmap(QPixmap('static/folder.png').scaled(self.iconQLabel.width(), self.iconQLabel.height(), Qt.KeepAspectRatio))

        self.pathLabel = QLabel()

        self.mainLayout.addWidget(self.iconQLabel, 0)
        self.mainLayout.addWidget(self.pathLabel, 1)

        self.setLayout(self.mainLayout)

    def setPath(self, path):
        self.pathLabel.setText(path)


class DirectoryView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()
        self.selectedFileInfo = None

        self.dirSelectForm = DirSelectFormView()
        self.dirSelectForm.dirSelectDialogBtn.clicked.connect(self.openDirSelectDialog)
        self.mainLayout.addWidget(self.dirSelectForm)

        self.listWidget = QListWidget(self)
        self.listWidget.itemDoubleClicked.connect(self.onClicked)

        self.mainLayout.addWidget(self.listWidget)

        self.setLayout(self.mainLayout)

    def onClicked(self, item: 'QListWidgetItem'):
        if self.selectedFileInfo is None:
            QMessageBox.information(self, "Error", "이동할 파일을 선택해주세요.")
            return

        from_path = self.selectedFileInfo.absoluteFilePath()
        to_path = self.listWidget.itemWidget(item).pathLabel.text()

        if os.path.exists(from_path) and os.path.isdir(to_path):
            shutil.move(from_path, to_path)
        else:
            QMessageBox.information(self, "Error", "이동 경로 및 파일이 올바르지 않습니다.")

    def setCurrentSelectedFile(self, fileInfo: 'QFileInfo'):
        self.selectedFileInfo = fileInfo

    def _isAlreadyExistDirPath(self, path):
        for row in range(self.listWidget.count()):
            item = self.listWidget.item(row)
            widget = self.listWidget.itemWidget(item)
            if path == widget.pathLabel.text():
                return True
        return False

    def addDirListItem(self, path):
        if self._isAlreadyExistDirPath(path):
            QMessageBox.information(self, "Error", f'{path}는 이미 존재합니다.')
            return

        directoryItemWidget = DirectoryItem(parent=self)
        directoryItemWidget.setPath(path)
        item = QListWidgetItem(self.listWidget)
        item.setSizeHint(directoryItemWidget.sizeHint())
        self.listWidget.addItem(item)
        self.listWidget.setItemWidget(item, directoryItemWidget)

    def openDirSelectDialog(self):
        rootPath = QFileDialog.getExistingDirectory(parent=self, caption="Select Directory")

        if not rootPath:
            return

        self.addDirListItem(rootPath)

    def clearCurrentSelectedFile(self):
        self.selectedFileInfo = None
