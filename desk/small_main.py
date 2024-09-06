import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from smallUI import Ui_MainWindow
from addTimeUI import Ui_DialogAddTime


class TimeTracker(QMainWindow):
    def __init__(self):
        super(TimeTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonADD.clicked.connect(self.open_addtime_menu)

    def open_addtime_menu(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_DialogAddTime()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TimeTracker()
    window.show()
    sys.exit(app.exec_())
