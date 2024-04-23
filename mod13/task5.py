import random
import sqlite3
from math import floor


def generate_test_data(
        cursor: sqlite3.Cursor,
        number_of_groups: int
) -> None:
    football_commands = ['Валенсия Франция', 'Бавария Германия', 'Арсенал Лондон', 'Локомотив Россия',
                         'Ливерпуль Англия', 'Интер Италия', 'ЦСКА Россия', 'РеалМадрид Испания',
                         'БоруссияД Германия', 'Зенит Россия', 'Спартак Россия', 'Челси Англия',
                         'Барселона Испания', 'Ювентус Турин', 'Ахмат Россия', 'Урал Россия',
                         'МанчестерСити Англия', 'Анжи Махачкала', 'Динамо Россия',
                         'Милан Италия', 'Сочи Россия', 'Рома Италия', 'МанчестерЮнайтед Манчестер',
                         'Наполи Италия', 'Аталанта Италия', 'Аякс Нидерланды', 'Тоттенхэм Англия',
                         'Шахтер Украина', 'Байер Германия', 'Порту Португалия', 'Интер Майами', 'Аль-Наср ОАЭ']

    levels = (1, 2, 3)
    uefa_commands_data = []
    uefa_draw_data = []
    for i, team_info in enumerate(football_commands, start=1):
        team, country = team_info.split()
        data = (i, team, country, random.choice(levels))
        uefa_commands_data.append(data)
        if number_of_groups * 2 <= i:
            draw_sub_data = (i, i, int(floor(i / 2)))
            uefa_draw_data.append(draw_sub_data)
    cursor.executemany(f"insert into uefa_commands values(?, ?, ?, ?)", uefa_commands_data)
    cursor.executemany(f"insert into uefa_draw values(?, ?, ?)", uefa_draw_data)


if __name__ == '__main__':
    group_count = int(input())
    with sqlite3.connect('hw.db') as conn:
        cur = conn.cursor()

        generate_test_data(cur, group_count)
