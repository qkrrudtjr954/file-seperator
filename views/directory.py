from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class DirectoryView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        lbl = QLabel('directory view')
        self.mainLayout.addWidget(lbl)

        self.setLayout(self.mainLayout)
