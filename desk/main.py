from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("TEST")
        self.setGeometry(300, 300, 300, 300)

        self.text = QtWidgets.QLabel(self)
        self.text.setText("AHUET")
        self.text.move(100, 100)
        self.text.adjustSize()

        self.new_text = QtWidgets.QLabel(self)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(100, 200)
        self.btn.setFixedWidth(100)
        self.btn.setText("XD")
        self.btn.clicked.connect(self.xd)

    def xd(self):
        self.new_text.setText("PIZDEC")
        self.new_text.move(50, 50)
        self.new_text.adjustSize()


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
