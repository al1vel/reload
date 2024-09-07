import sys
import datetime
import smallDB
import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from smallUI import Ui_MainWindow
from addTimeUI import Ui_DialogAddTime

EVERYDAY_GOAL = 200


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
        self.update_today_info()
        self.new_window.close()

    def update_today_info(self):
        date = datetime.date.today().strftime("%d-%m-%Y")
        today_regs = smallDB.get_regs_for_date(date)
        print(today_regs)

        work_time = 0
        for reg in today_regs:
            work_time += reg[2]
        print(work_time)
        work_time_str = f'{work_time // 60} h {work_time % 60} min'

        goal_time = EVERYDAY_GOAL - work_time
        if goal_time < 0:
            goal_time = 0
        goal_time_str = f'{goal_time // 60} h {goal_time % 60} min'

        percent_str = f'{round(((work_time / EVERYDAY_GOAL) * 100), 1)} %'

        self.ui.todayWorkTime.setText(work_time_str)
        self.ui.todayFinishTime.setText(goal_time_str)
        self.ui.todayProgress.setText(percent_str)


if __name__ == "__main__":
    smallDB.db_init()

    app = QApplication(sys.argv)
    window = TimeTracker()
    window.show()
    window.update_today_info()
    sys.exit(app.exec_())
