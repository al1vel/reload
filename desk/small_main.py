import sys
import datetime
import smallDB
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from smallUI import Ui_MainWindow
from addTimeUI import Ui_DialogAddTime

connection = sqlite3.connect('my_db.db', check_same_thread=False)
cursor = connection.cursor()


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

        self.ui_window.buttonADD.clicked.connect(self.add_time)

    def add_time(self):
        date = datetime.date.today().strftime("%d-%m-%Y")
        print(date)

        hours_cnt = self.ui_window.lineEditHours.text()
        print(hours_cnt)

        minutes_cnt = self.ui_window.lineEditMinutes.text()
        print(minutes_cnt)

        comment = self.ui_window.textEditOccupation.toPlainText()
        print(comment)

        amount_of_time = int(hours_cnt) * 60 + int(minutes_cnt)
        print(amount_of_time)

        smallDB.add_time_to_db(date, amount_of_time, comment)
        smallDB.get_all_regs()
        self.new_window.close()


if __name__ == "__main__":
    smallDB.db_init()

    app = QApplication(sys.argv)
    window = TimeTracker()
    window.show()
    sys.exit(app.exec_())
