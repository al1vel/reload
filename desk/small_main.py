import sys
import datetime
import smallDB
# from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from smallUI import Ui_MainWindow
from addTimeUI import Ui_DialogAddTime
from addTimeByTimerUI import Ui_DialogAddByTimer

EVERYDAY_GOAL = 200


class TimeTracker(QMainWindow):
    def __init__(self):
        super(TimeTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonADD.clicked.connect(self.open_addtime_menu)
        self.ui.buttonSTARTTIMER.clicked.connect(self.click_timer_button)
        self.ui.buttonPrevDay.clicked.connect(self.open_prev_day)
        self.ui.buttonNextDay.clicked.connect(self.open_next_day)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.display_time)

        self.START_TIME = "hui"
        self.TIMER_TIME = ""

        self.TODAY_DATE = datetime.datetime.now()
        self.DISPLAYED_DATE = self.TODAY_DATE
        self.DISPLAYED_WEEK = self.TODAY_DATE

    def open_addtime_menu(self):
        self.window_default_add = QtWidgets.QDialog()
        self.ui_def_add = Ui_DialogAddTime()
        self.ui_def_add.setupUi(self.window_default_add)
        self.window_default_add.show()

        self.ui_def_add.buttonADD.clicked.connect(self.add_time)

    def add_time(self):
        date = self.DISPLAYED_DATE.strftime("%d-%m-%Y")
        hours_cnt = self.ui_def_add.lineEditHours.text()
        print(hours_cnt)

        minutes_cnt = self.ui_def_add.lineEditMinutes.text()
        print(minutes_cnt)

        comment = self.ui_def_add.textEditOccupation.toPlainText()
        print(comment)

        amount_of_time = int(hours_cnt) * 60 + int(minutes_cnt)
        print(amount_of_time)

        smallDB.add_time_to_db(date, amount_of_time, comment)
        self.update_today_info()
        self.window_default_add.close()

    def update_today_info(self):
        date = self.DISPLAYED_DATE.strftime("%d-%m-%Y")
        today_regs = smallDB.get_regs_for_date(date)
        print(today_regs)

        work_time = 0
        for reg in today_regs:
            work_time += reg[2]
        work_time_str = f'{work_time // 60} h {work_time % 60} min'

        goal_time = EVERYDAY_GOAL - work_time
        if goal_time < 0:
            goal_time = 0
        goal_time_str = f'{goal_time // 60} h {goal_time % 60} min'

        percent_str = f'{round(((work_time / EVERYDAY_GOAL) * 100), 1)} %'

        self.ui.todayWorkTime.setText(work_time_str)
        self.ui.todayFinishTime.setText(goal_time_str)
        self.ui.todayProgress.setText(percent_str)

    def click_timer_button(self):
        if self.ui.buttonSTARTTIMER.text() == "START TIMER":
            self.ui.buttonSTARTTIMER.setText("0:00:00")
            self.timer.start()
            self.START_TIME = QtCore.QDateTime.currentDateTime().toString('yyyy:MM:dd:hh:mm:ss')
        else:
            self.timer.stop()
            self.TIMER_TIME = self.ui.buttonSTARTTIMER.text()
            self.ui.buttonSTARTTIMER.setText("START TIMER")
            self.open_add_timertime_menu()

    def display_time(self):
        st = self.START_TIME.split(":")
        time_start = datetime.datetime(int(st[0]), int(st[1]), int(st[2]), int(st[3]), int(st[4]), int(st[5]))

        cur_time = QtCore.QDateTime.currentDateTime().toString('yyyy:MM:dd:hh:mm:ss')
        fn = cur_time.split(":")
        time_now = datetime.datetime(int(fn[0]), int(fn[1]), int(fn[2]), int(fn[3]), int(fn[4]), int(fn[5]))

        diff = time_now - time_start
        self.ui.buttonSTARTTIMER.setText(str(diff))

    def open_add_timertime_menu(self):
        hrs = str(self.TIMER_TIME).split(":")[0]
        mins = str(self.TIMER_TIME).split(":")[1]
        if mins == "00":
            mins = "01"
        print(hrs, mins)

        self.window_timer_add = QtWidgets.QDialog()
        self.ui_timer_add = Ui_DialogAddByTimer()
        self.ui_timer_add.setupUi(self.window_timer_add)

        self.ui_timer_add.timeHours.setText(hrs)
        self.ui_timer_add.timeMinutes.setText(mins)

        self.window_timer_add.show()

        self.ui_timer_add.buttonADD.clicked.connect(self.add_time_by_timer)

    def add_time_by_timer(self):
        date = datetime.date.today().strftime("%d-%m-%Y")
        print(date)

        hours_cnt = self.ui_timer_add.timeHours.text()
        print(hours_cnt)

        minutes_cnt = self.ui_timer_add.timeMinutes.text()
        print(minutes_cnt)

        comment = self.ui_timer_add.textEditOccupation.toPlainText()
        print(comment)

        amount_of_time = int(hours_cnt) * 60 + int(minutes_cnt)
        print(amount_of_time)

        smallDB.add_time_to_db(date, amount_of_time, comment)
        self.update_today_info()
        self.window_timer_add.close()

    def open_prev_day(self):
        self.DISPLAYED_DATE = self.DISPLAYED_DATE - datetime.timedelta(days=1)
        if self.DISPLAYED_DATE == self.TODAY_DATE:
            self.ui.labelToday.setText("TODAY")
        else:
            date = self.DISPLAYED_DATE.strftime("%d-%m")
            self.ui.labelToday.setText(date)
        self.update_today_info()

    def open_next_day(self):
        self.DISPLAYED_DATE = self.DISPLAYED_DATE + datetime.timedelta(days=1)
        if self.DISPLAYED_DATE == self.TODAY_DATE:
            self.ui.labelToday.setText("TODAY")
        else:
            date = self.DISPLAYED_DATE.strftime("%d-%m")
            self.ui.labelToday.setText(date)
        self.update_today_info()

    def update_week_info(self):
        date = self.DISPLAYED_DATE.strftime("%d-%m-%Y")

    def open_prev_week(self):
        day_num = self.DISPLAYED_WEEK.weekday()
        self.DISPLAYED_WEEK = self.DISPLAYED_WEEK - datetime.timedelta(days=7)


if __name__ == "__main__":
    smallDB.db_init()

    app = QApplication(sys.argv)
    window = TimeTracker()
    window.show()
    window.update_today_info()
    sys.exit(app.exec_())
