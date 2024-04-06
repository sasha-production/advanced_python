import sqlite3

with sqlite3.connect('hw_3_database.db') as conn:
    cur = conn.cursor()
    count1 = cur.execute(f"select count(*) from table_1").fetchone()
    count2 = cur.execute(f"select count(*) from table_2").fetchone()
    count3 = cur.execute(f"select count(*) from table_3").fetchone()
    print(count1, count2, count3)
    unic_values_1 = cur.execute(f"select count(distinct(value)) from table_1 ").fetchone()
    print(unic_values_1)
    intersection1_2 = cur.execute(f"select * "
                                  f"from table_1 "
                                  f"intersect "
                                  f"select * "
                                  f"from table_2").fetchall()  # [(24, 'Mitsubishi')]
    print(intersection1_2)
    intersection1_2_3 = cur.execute(f"select value "
                                  f"from table_1 "
                                  f"intersect "
                                  f"select value "
                                  f"from table_2 "
                                    f"intersect "
                                    f"select value "
                                    f"from table_3 " ).fetchall()
    print(intersection1_2_3)
