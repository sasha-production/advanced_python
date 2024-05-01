import sqlite3

from flask import Flask
from typing import List, Dict


DATA = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


class Book:
    def __init__(self, id: int, title: str, author: str, count: int = 0):
        self.id = id
        self.title = title
        self.author = author
        self.count = count

    def __getitem__(self, item):
        return getattr(self, item)

def init_db(initial_records: List[Dict]):
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name='table_books';"
        )
        exists = cursor.fetchone()
        # Если таблицы нет, создаем ее и заполняем
        if not exists:
            exists = cursor.executescript(
                "CREATE TABLE 'table_books'"
                '(id INTEGER PRIMARY KEY AUTOINCREMENT, title, author, count)'
            )
            cursor.executemany(
                'INSERT INTO table_books'
                '(title, author) VALUES (?, ?)',
                [(item['title'], item['author']) for item in initial_records]
                #Делаем записи
            )


def get_all_books() -> List[Dict]:
    with sqlite3.connect('table_books.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * from table_books')
        all_books = cursor.fetchall()
        return [Book(*row) for row in all_books]
        #Объединяем данные из БД, создаем из кортежа объект нашего класса

def add_book_from_form(book: Book):
    with sqlite3.connect('table_books.db') as conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO table_books VALUES(?, ?)", (book.title, book.author))
    conn.cursor()


def get_books_from_author(author: str):
    with sqlite3.connect('table_books.db') as conn:
        cur = conn.cursor()
        books = cur.execute(f"select title from table_books "
                            f"where author = '{author}'").fetchall()

        return books

def get_book_by_id(id :int) -> Book:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * from `table_books` WHERE id = {id}
            """
        )
        return Book(*cursor.fetchone())


def update_books_count(books: List[Book]) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        parameters = []
        query = """
            UPDATE table_books SET count= :count
                WHERE id= :id
        """
        for book in books:
            parameters.append({
                "id": book.id,
                "count": book.count + 1
            })
        cursor.executemany(query, parameters)

def update_book_count(book: Book) -> None:
    with sqlite3.connect('table_books.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        cursor.execute(f"""
            UPDATE table_books SET count= {book.count + 1}
                WHERE id= {book.id}""")

if __name__ == '__main__':
    init_db(DATA)

