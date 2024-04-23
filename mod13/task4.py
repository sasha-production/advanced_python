import sqlite3


def ivan_sovin_the_most_effective(
        cursor: sqlite3.Cursor,
          name: str,
) -> None:
    sovin_salary = cursor.execute(f"select salary from table_effective_manager "
                                  f"where name like 'Иван Совин'").fetchone()[0]
    employee_salary = cursor.execute(f"select salary from table_effective_manager "
                                     f"where name like '{name}'").fetchone()[0]
    if employee_salary * 1.1 > sovin_salary and name != 'Иван Совин':
        cursor.execute(f"delete from table_effective_manager "
                       f"where name like '{name}'")
        print("сотрудник уволен")
    else:
        cursor.execute(f"update table_effective_manager "
                       f"set salary = {employee_salary * 1.1} "
                       f"where name like '{name}'")
        print('зп увеличена')


if __name__ == '__main__':
    employee_name = input()
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()
        ivan_sovin_the_most_effective(cur, employee_name)
        conn.commit()
