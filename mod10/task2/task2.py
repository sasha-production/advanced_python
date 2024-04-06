import sqlite3

with sqlite3.connect('hw_2_database.db') as conn:
    cur = conn.cursor()
    most_sold = cur.execute(f"select phone_color, max(sold_count) from table_checkout").fetchone() # ('Violet', 1120)
    print(most_sold[0])  # Violet
    red_and_blue_stats = cur.execute(f"select phone_color, sold_count from table_checkout "
                                     f"where phone_color like 'red' or phone_color like 'blue' "
                                     f"order by sold_count desc").fetchall()  # [('Red', 64), ('Blue', 36)]
    print(red_and_blue_stats[0][0])  # red

    less_popular_color = cur.execute(f"select phone_color, min(sold_count) from table_checkout").fetchall()  # [('Goldenrod', 2)]
    print(less_popular_color[0][0])