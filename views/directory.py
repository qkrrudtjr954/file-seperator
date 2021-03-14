from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QHBoxLayout, QLabel, QListWidget, QListWidgetItem, QMessageBox, QPushButton, QVBoxLayout, QWidget


class DirSelectFormView(QWidget):
    def __init__(self, *args, **kwargs):
        super(DirSelectFormView, self).__init__(*args, **kwargs)
        self.mainLayout = QHBoxLayout(self)
        self.dirSelectDialogBtn = QPushButton('+')
        self.mainLayout.addWidget(self.dirSelectDialogBtn)


class DirectoryItem(QWidget):
    def __init__(self, *args, **kwargs):
        super(DirectoryItem, self).__init__(*args, **kwargs)
        self.mainLayout = QHBoxLayout()

        self.iconQLabel = QLabel(self)
        self.iconQLabel.setPixmap(QPixmap('static/folder.png').scaled(self.iconQLabel.width(), self.iconQLabel.height(), Qt.KeepAspectRatio))

        self.pathLabel = QLabel()

        self.moveBtn = QPushButton('+')

        self.mainLayout.addWidget(self.iconQLabel, 0)
        self.mainLayout.addWidget(self.pathLabel, 1)
        self.mainLayout.addWidget(self.moveBtn, 2)

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

    def onClicked(self, item):
        QMessageBox.information(self, "Info", item.text())

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

        directoryItemWidget = DirectoryItem()
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
