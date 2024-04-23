import sqlite3
import csv


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, encoding='windows-1251') as file:
        dict_reader = csv.DictReader(file)
        for row in dict_reader:
            cursor.execute(f"delete from table_fees "
                           f"where timestamp = {row['timestamp']} and truck_number = {row['car_number']}")


if __name__ == '__main__':
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        file_name = 'wrong_fees.csv'
        delete_wrong_fees(cur, file_name)
        conn.commit()