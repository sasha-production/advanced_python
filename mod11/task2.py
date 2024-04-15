import requests
import time
import sqlite3
import concurrent.futures


def create_databases():
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.cursor()
        cur.execute(f"CREATE TABLE IF NOT EXISTS table_1 ("
                    f"name TEXT NOT NULL, "
                    f"age TEXT NOT NULL, "
                    f"sex TEXT NOT NULL )")
        cur.execute(f"CREATE TABLE IF NOT EXISTS table_2 ("
                    f"name TEXT NOT NULL, "
                    f"age TEXT NOT NULL, "
                    f"sex TEXT NOT NULL )")


def consistently_fun():
    start = time.perf_counter()
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.cursor()
        for i in range(1, 22):
            response = requests.get(f'https://swapi.dev/api/people/{i}/')
            if response.status_code // 100 == 2:
                data = response.json()
                person, age, sex = data['name'], data['birth_year'], data['gender']
                cur.execute(f"INSERT INTO table_1 (name, age, sex) "
                            f"VALUES (?, ?, ?)",
                            (person, age, sex))

    end = time.perf_counter()
    print(end - start)


def make_response(index):
    with requests.get(f"https://swapi.dev/api/people/{index}/") as response:
        if response.status_code == 200:
            data = response.json()
            character_data = data['name'], data['birth_year'], data['gender']
            return character_data


def multitradeing_fun():
    start = time.perf_counter()
    with sqlite3.connect('my_database.db') as conn:
        cur = conn.cursor()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_url = {executor.submit(make_response, i): i for i in range(1, 22)}
            for future in concurrent.futures.as_completed(future_to_url):
                data = future.result()
                if data:
                    cur.execute(f"INSERT INTO table_2 (name, age, sex) "
                            f"VALUES (?, ?, ?)",
                            data)

    end = time.perf_counter()
    print(end - start)


def main():
    create_databases()
    consistently_fun()  # 9.168106799945235
    multitradeing_fun()  # 2.4134755998384207


if __name__ == '__main__':
    main()