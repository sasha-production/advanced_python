import sqlite3


def check_if_vaccine_has_spoiled(cursor: sqlite3.Cursor, truck_number: str) -> bool:
    res = cursor.execute(f"""
    SELECT EXISTS (SELECT * FROM table_truck_with_vaccine WHERE truck_number='{truck_number}'
    AND temperature_in_celsius NOT BETWEEN 16 AND 20)
    """).fetchone()[0]
    return bool(res)


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        truck_number = input()

        res = check_if_vaccine_has_spoiled(cur, truck_number)
        print('испортилась' if not res else 'не испортилась')
