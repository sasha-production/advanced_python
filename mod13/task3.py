import datetime
import sqlite3


def log_bird(
        cursor: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    cursor.execute(f"insert into some_bird_table? (bird_name, date_time) values ({bird_name}, {date_time})")


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    res = cursor.execute(f"select exists(select * from some_bird_table? where name = {bird_name}").fetchone()
    return bool(res[0])


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        name_bird = 'some_name'
        if not check_if_such_bird_already_seen(cur, name_bird):
            log_bird(cur, name_bird, date_time=str(datetime.datetime.utcnow()))
        else:
            print('The bird has already logged')
        conn.commit()