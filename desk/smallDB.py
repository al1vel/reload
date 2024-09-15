import sqlite3
import datetime


def db_init():
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Operations (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    amount_of_time INTEGER,
    occupation TEXT NOT NULL)''')


def add_time_to_db(date, amount_of_time, occupation):
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()

    cursor.execute(f'INSERT INTO Operations (date, amount_of_time, occupation) VALUES (?, ?, ?)', (date, amount_of_time, occupation))
    connection.commit()
    connection.close()


def get_all_regs():
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Operations')
    data = cursor.fetchall()
    print(data)

    connection.commit()
    connection.close()


def get_regs_for_date(date):
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Operations WHERE date = "{date}"')
    result = cursor.fetchall()
    return result


def day_info(date, goal):
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Operations WHERE date = "{date}"')
    day_data = cursor.fetchall()

    day_worktime = 0

    for reg in day_data:
        day_worktime += reg[2]
    day_goaltime = goal - day_worktime
    if day_goaltime < 0:
        day_goaltime = 0
    day_percent = round(((day_worktime / goal) * 100), 1)

    answer = [day_worktime, day_goaltime, day_percent]
    return answer


def week_info(date, goal):
    overall_work_time = 0
    full_days_cnt = 0
    day_num = date.weekday()
    week_start = date - datetime.timedelta(days=day_num)
    day = week_start

    for i in range(7):
        day_str = day.strftime("%d-%m-%Y")

        day_data = day_info(day_str, goal)
        overall_work_time += day_data[0]
        if day_data[2] >= 100:
            full_days_cnt += 1

        day = day + datetime.timedelta(days=1)

    answer = [overall_work_time, full_days_cnt]
    return answer


def delete_reg(ind):
    connection = sqlite3.connect('my_db.db', check_same_thread=False)
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM Operations WHERE id = {ind}')
    # print("hui")
    connection.commit()
    connection.close()


def get_graph_data(days_cnt, date, goal):
    result = []
    for i in range(days_cnt):
        date_str = date.strftime("%d-%m-%Y")

        date_data = day_info(date_str, goal)
        day = [date_str, date_data[0]]
        result.append(day)
        date = date - datetime.timedelta(days=1)

    return result
