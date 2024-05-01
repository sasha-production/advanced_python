import sqlite3
import time
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool


import requests


def create_db():
    conn = sqlite3.connect('mod12.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS characters (name TEXT, age TEXT, gender TEXT)')
    conn.commit()
    conn.close()


def download_data(character_url) -> dict | None:
    response = requests.get(character_url)
    if response.status_code == 200:
        data = response.json()
        character_data = {'name': data['name'], 'age': data['birth_year'], 'gender': data['gender']}
        return character_data
    else:
        return None


def save_data(character_data):
    if character_data:
        conn = sqlite3.connect('mod12.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO characters (name, age, gender) VALUES (?, ?, ?)',
                  (character_data['name'], character_data['age'], character_data['gender']))
        conn.commit()
        conn.close()


def processes_function():
    start = time.perf_counter()
    character_urls = [f'https://swapi.dev/api/people/{i}/' for i in range(1, 21)]

    with Pool() as pool:
        results = pool.map(download_data, character_urls)

        for result in results:
            save_data(result)

    end = time.perf_counter()
    print(f"Пул потоков: {end - start} с")


def threads_function():
    start = time.perf_counter()
    character_urls = [f'https://swapi.dev/api/people/{i}/' for i in range(1, 21)]
    with ThreadPoolExecutor() as executor:
        results = executor.map(download_data, character_urls)

        for result in results:
            save_data(result)
    end = time.perf_counter()
    print(f"ThreadPool: {end - start} c")


if __name__ == '__main__':
    create_db()
    threads_function()
    # processes_function()
