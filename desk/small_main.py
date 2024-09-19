import sys
import datetime
import smallDB

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import pyqtgraph as pg
from PyQt5 import QtCore, QtGui, QtWidgets


from smallUI import Ui_MainWindow
from addTimeUI import Ui_DialogAddTime
from addTimeByTimerUI import Ui_DialogAddByTimer
from listUI import Ui_DialogList
from settingsUI import Ui_DialogSettings


class TimeTracker(QMainWindow):
    def __init__(self):
        super(TimeTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.buttonADD.clicked.connect(self.open_addtime_menu)
        self.ui.buttonSTARTTIMER.clicked.connect(self.click_timer_button)
        self.ui.buttonPAUSETIMER.clicked.connect(self.pause_timer)
        self.ui.buttonSAVETIMER.clicked.connect(self.save_timer)
        self.ui.buttonPrevDay.clicked.connect(self.open_prev_day)
        self.ui.buttonNextDay.clicked.connect(self.open_next_day)
        self.ui.buttonPrevWeek.clicked.connect(self.open_prev_week)
        self.ui.buttonNextWeek.clicked.connect(self.open_next_week)
        self.ui.buttonLIST.clicked.connect(self.open_list_menu)
        self.ui.buttonSETTINGS.clicked.connect(self.open_settings_menu)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.display_time)

        self.TIMER_TIME = ""
        self.TimerCounter = 0
        self.pause_flag = 'pause'
        self.timer_started = False

        self.EVERYDAY_GOAL = 200
        self.DAYS_IN_GRAPH = 20

        self.TODAY_DATE = datetime.date.today()
        self.DISPLAYED_DATE = self.TODAY_DATE
        self.DISPLAYED_WEEK = self.TODAY_DATE
        self.DATE_WHEN_OPEN_APP = self.TODAY_DATE

        self.ui.graph.setBackground((60, 60, 60))
        self.ui.graph.setTitle("EFFICIENCY")
        # self.ui.graph.showGrid(x=True, y=True)
        self.ui.graph.getAxis('left').setVisible(False)
        self.ui.graph.getAxis('bottom').setVisible(False)

    def update_graph(self):
        if self.DAYS_IN_GRAPH == 0:
            self.DAYS_IN_GRAPH = 20
        data = smallDB.get_graph_data(self.DAYS_IN_GRAPH, self.TODAY_DATE, self.EVERYDAY_GOAL)
        # print(data)
        # print(self.DAYS_IN_GRAPH)
        dates = [i for i in range(self.DAYS_IN_GRAPH)]
        times = []
        for i in range(self.DAYS_IN_GRAPH - 1, -1, -1):
            times.append(int(data[i][1]))
        # print(dates)
        # print(times)

        pen = pg.mkPen(color=(180, 180, 180), width=6)
        self.ui.graph.clear()
        self.ui.graph.plot(dates, times, pen=pen)

    def open_addtime_menu(self):
        self.window_default_add = QtWidgets.QDialog()
        self.ui_def_add = Ui_DialogAddTime()
        self.ui_def_add.setupUi(self.window_default_add)
        self.window_default_add.show()

        self.ui_def_add.buttonADD.clicked.connect(self.add_time)

    def open_settings_menu(self):
        self.window_settings = QtWidgets.QDialog()
        self.ui_settings = Ui_DialogSettings()
        self.ui_settings.setupUi(self.window_settings)
        self.window_settings.show()


        self.ui_settings.lineEditHours.setText(f'{self.EVERYDAY_GOAL // 60}')
        self.ui_settings.lineEditMinutes.setText(f'{self.EVERYDAY_GOAL % 60}')
        self.ui_settings.lineEditDaysInGraph.setText(f'{self.DAYS_IN_GRAPH}')

        self.ui_settings.buttonSAVE.clicked.connect(self.save_settings)

    def open_list_menu(self):
        self.list_menu = QtWidgets.QDialog()
        self.ui_list_menu = Ui_DialogList()
        self.ui_list_menu.setupUi(self.list_menu)

        self.model = QStandardItemModel(0, 0)
        self.model.setHorizontalHeaderLabels(["TIME", "COMMENT"])
        self.ui_list_menu.tableView.setModel(self.model)

        self.ui_list_menu.tableView.setColumnWidth(0, 50)
        self.ui_list_menu.tableView.setColumnWidth(1, 120)
        self.ui_list_menu.tableView.setColumnWidth(2, 150)

        self.update_list()
        # self.ui_list_menu.tableView.clearSpans()
        self.list_menu.show()

        self.ui_list_menu.buttonDEL.clicked.connect(self.delete_reg_from_list)

    def update_list(self):
        data = smallDB.get_regs_for_date(self.DISPLAYED_DATE.strftime("%d-%m-%Y"))
        print(self.DISPLAYED_DATE)
        print(data)
        x = 0
        for reg in data:
            worktime_str = f'{reg[2] // 60} h {reg[2] % 60} min'
            # print(worktime_str)
            worktime = QStandardItem(worktime_str)
            # worktime.setTextAlignment(Qt.AlignCenter)
            comment = QStandardItem(f'{reg[3]}')
            ind = QStandardItem(f'{reg[0]}')
            # comment.setTextAlignment(Qt.AlignCenter)
            self.model.setItem(x, 0, ind)
            self.model.setItem(x, 1, worktime)
            self.model.setItem(x, 2, comment)
            x += 1
        print("Update ok")

    def delete_reg_from_list(self):
        index = self.ui_list_menu.tableView.selectedIndexes()[0].row()
        ind = self.model.index(index, 0)
        reg_id = int(self.ui_list_menu.tableView.model().itemData(ind)[0])
        smallDB.delete_reg(reg_id)
        self.model.removeRow(index)
        self.update_week_info()
        self.update_today_info()
        self.update_graph()

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
        self.update_week_info()
        self.update_graph()
        self.window_default_add.close()

    def save_settings(self):
        goal = int(self.ui_settings.lineEditHours.text()) * 60 + int(self.ui_settings.lineEditMinutes.text())
        days_in_graph = int(self.ui_settings.lineEditDaysInGraph.text())

        self.EVERYDAY_GOAL = goal
        self.DAYS_IN_GRAPH = days_in_graph

        smallDB.save_settings(self.DAYS_IN_GRAPH, self.EVERYDAY_GOAL)

        self.update_today_info()
        self.update_week_info()
        self.update_graph()
        self.window_settings.close()

    def update_settings(self):
        settings = smallDB.get_settings()
        print(settings)
        if len(settings) == 0:
            self.DAYS_IN_GRAPH = 20
            self.EVERYDAY_GOAL = 200
        else:
            self.DAYS_IN_GRAPH = settings[0][1]
            self.EVERYDAY_GOAL = settings[0][2]

    def update_today_info(self):
        date = self.DISPLAYED_DATE.strftime("%d-%m-%Y")
        data = smallDB.day_info(date, self.EVERYDAY_GOAL)
        work_time_str = f'{data[0] // 60} h {data[0] % 60} min'
        goal_time_str = f'{data[1] // 60} h {data[1] % 60} min'
        percent_str = f'{data[2]}%'

        self.ui.todayWorkTime.setText(work_time_str)
        self.ui.todayFinishTime.setText(goal_time_str)
        self.ui.todayProgress.setText(percent_str)

    def click_timer_button(self):
        if not self.timer_started:
            self.ui.buttonSTARTTIMER.setText("0:00:00")
            self.timer.start()
            self.timer_started = True

    def display_time(self):
        self.TimerCounter += 1
        hrs = self.TimerCounter // 3600
        mins = self.TimerCounter // 60
        if len(str(mins)) == 1:
            mins = f'0{mins}'
        secs = self.TimerCounter % 60
        if len(str(secs)) == 1:
            secs = f'0{secs}'
        time_str = f'{hrs}:{mins}:{secs}'
        self.ui.buttonSTARTTIMER.setText(str(time_str))

    def pause_timer(self):
        if not self.timer_started:
            return
        if self.pause_flag == "pause":
            ic = QtGui.QIcon()
            ic.addPixmap(QtGui.QPixmap(":/icons/icons8-play-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.buttonPAUSETIMER.setIcon(ic)
            self.ui.buttonPAUSETIMER.setIconSize(QtCore.QSize(25, 25))

            self.timer.stop()
            self.pause_flag = "continue"

        elif self.pause_flag == "continue":
            ic = QtGui.QIcon()
            ic.addPixmap(QtGui.QPixmap(":/icons/icons8-pause-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.ui.buttonPAUSETIMER.setIcon(ic)
            self.ui.buttonPAUSETIMER.setIconSize(QtCore.QSize(25, 25))

            self.timer.start()
            self.pause_flag = "pause"

    def save_timer(self):
        if not self.timer_started:
            return

        ic = QtGui.QIcon()
        ic.addPixmap(QtGui.QPixmap(":/icons/icons8-pause-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.buttonPAUSETIMER.setIcon(ic)
        self.ui.buttonPAUSETIMER.setIconSize(QtCore.QSize(25, 25))
        self.pause_flag = "pause"

        self.timer.stop()
        self.TIMER_TIME = self.ui.buttonSTARTTIMER.text()
        self.ui.buttonSTARTTIMER.setText("START TIMER")
        self.timer_started = False
        self.TimerCounter = 0
        self.open_add_timertime_menu()

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
        self.update_week_info()
        self.update_graph()
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
        date = self.DISPLAYED_WEEK
        date_prev = date - datetime.timedelta(days=7)

        res = smallDB.week_info(date, self.EVERYDAY_GOAL)
        res_prev = smallDB.week_info(date_prev, self.EVERYDAY_GOAL)

        worktime_str = f'{res[0] // 60} h {res[0] % 60} min'
        avg_minutes = res[0] / 7
        avg_str = f'{str(avg_minutes // 60).split(".")[0]} h {round((avg_minutes % 60), 1)} min'
        percent_str = f'{round((((res[0]) / (self.EVERYDAY_GOAL * 7)) * 100), 1)}%'

        if res_prev[0] == 0:
            self.ui.WeekGrowth.setText(f'Nothing to compare')
        else:
            cur_percent = (res[0] * 100 / res_prev[0])
            growth = cur_percent - 100
            print(growth)
            self.ui.WeekGrowth.setText(f'{round(growth, 1)}%')

        self.ui.WeekOverall.setText(worktime_str)
        self.ui.WeekAverage.setText(avg_str)
        self.ui.WeekPercent.setText(percent_str)
        self.ui.WeekFullDays.setText(f'{res[1]}')

    def open_prev_week(self):
        day_num = self.DISPLAYED_WEEK.weekday()
        self.DISPLAYED_WEEK = self.DISPLAYED_WEEK - datetime.timedelta(days=7)
        week_start = (self.DISPLAYED_WEEK - datetime.timedelta(days=day_num)).strftime("%d-%m")
        week_end = (self.DISPLAYED_WEEK + datetime.timedelta(days=(6 - day_num))).strftime("%d-%m")

        if self.DISPLAYED_WEEK == self.DATE_WHEN_OPEN_APP:
            self.ui.labelThisWeek.setText("THIS WEEK")
        else:
            s = f'{week_start}  {week_end}'
            self.ui.labelThisWeek.setText(s)
        self.update_week_info()

    def open_next_week(self):
        day_num = self.DISPLAYED_WEEK.weekday()
        self.DISPLAYED_WEEK = self.DISPLAYED_WEEK + datetime.timedelta(days=7)
        week_start = (self.DISPLAYED_WEEK - datetime.timedelta(days=day_num)).strftime("%d-%m")
        week_end = (self.DISPLAYED_WEEK + datetime.timedelta(days=(6 - day_num))).strftime("%d-%m")

        if self.DISPLAYED_WEEK == self.DATE_WHEN_OPEN_APP:
            self.ui.labelThisWeek.setText("THIS WEEK")
        else:
            s = f'{week_start}  {week_end}'
            self.ui.labelThisWeek.setText(s)
        self.update_week_info()


if __name__ == "__main__":
    smallDB.db_init()

    app = QApplication(sys.argv)
    window = TimeTracker()
    window.show()
    window.update_settings()
    window.update_today_info()
    window.update_week_info()
    window.update_graph()
    sys.exit(app.exec_())
