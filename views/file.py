from PyQt5.QtCore import QDir
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
        self.dirSelectForm.dirSelectDialogBtn.clicked.connect(self.dirSelectDialogBtnClicked)
        layout.addWidget(self.dirSelectForm)

        # 파일 목록 화면 설정
        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files | QDir.AllDirs)

        self.fileListView = QListView()
        self.fileListView.setModel(self.fileModel)
        self.refreshFileListView()
        layout.addWidget(self.fileListView)

    def refreshFileListView(self, path: str = None):
        path = path if path else QDir.rootPath()
        self.fileListView.setRootIndex(self.fileModel.setRootPath(path))

    def dirSelectDialogBtnClicked(self):
        root_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.dirSelectForm.dirPathLineEdit.setText(root_path)
        self.refreshFileListView(root_path)
