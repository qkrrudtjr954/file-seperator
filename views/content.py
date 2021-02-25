from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class ContentView(QWidget):
    def __init__(self):
        super().__init__()

        self.mainLayout = QVBoxLayout()

        lbl = QLabel('content view')
        self.mainLayout.addWidget(lbl)

        self.setLayout(self.mainLayout)
