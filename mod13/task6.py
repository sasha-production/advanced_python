import sqlite3
from datetime import datetime, timedelta

date = datetime(year=2020, month=1, day=1)
delta = timedelta(days=1)
weekday_and_sport = {0: 'футбол', 1: 'хоккей', 2: 'шахматы', 3: 'SUP сёрфинг', 4: 'бокс', 5: 'Dota2', 6: 'шах-бокс'}


def drop_table_friendship_schedule(cursor: sqlite3.Cursor):
    cursor.execute("DELETE FROM table_friendship_schedule")


def update_work_schedule(cursor: sqlite3.Cursor) -> None:
    drop_table_friendship_schedule(cursor)

    all_employees = cursor.execute(f"select * from table_friendship_employees").fetchall()
    j = 0
    schedule = []
    date = datetime(year=2020, month=1, day=1)
    for i in range(366):

        # id_employee, _, preferable_sport = all_employees[i]
        while True:
            if len(schedule) == 10:
                cursor.executemany(f"insert into table_friendship_schedule values(?, ?)", schedule)
                schedule.clear()
                break
            employee = all_employees[j % 366]
            employee_id, employee_sport = employee[0], employee[2]
            if weekday_and_sport[date.weekday()] != employee_sport:
                schedule.append((employee_id, date))
            j += 1

        date += delta


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        update_work_schedule(cur)