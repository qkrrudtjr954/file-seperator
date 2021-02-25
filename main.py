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

        self.mainLayout.addWidget(FileView(), stretch=2)
        self.mainLayout.addWidget(ContentView(), stretch=3)
        self.mainLayout.addWidget(DirectoryView(), stretch=2)

        self.setWindowTitle('파일 분류기')
        self.setLayout(self.mainLayout)
        self.showMaximized()


app = QApplication(sys.argv)
ex = MainView()
sys.exit(app.exec_())
