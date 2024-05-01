import re
import sqlite3

from flask import Response

from forms import MyForm
from flask import request
from mod14.forms import MyForm
from flask import Flask, render_template, request, redirect, url_for
from typing import List, Dict

from mod14.models import init_db, DATA, get_all_books, Book, add_book_from_form, get_books_from_author,\
    update_book_count, update_books_count, get_book_by_id

app = Flask(__name__)

BOOKS = [
    {'id': 0, 'title': 'A byte of Python', 'author': 'Swaroop C. H.'},
    {'id': 1, 'title': 'Moby-Dick; or, The Whale', 'author': 'Herman Melville'},
    {'id': 2, 'title': 'Mar and Peace', 'author': 'Lev Tolstoy'},
]


def _get_hmtl_table_for_books(books: List[Dict]) -> str:
    table = """
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Author</th>
                </tr>
            </thead>
                <tbody>
                    {books_rows}
                </tbody>
        </table>
    """
    rows = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    return render_template('pred_index.html', books=get_all_books())


@app.route('/books/form', methods=['GET', 'POST'])
def get_books_form():
    if request.method == 'POST':
        form = MyForm(request.form)
        if form.validate_on_submit():
            book_title, book_author = request.form['field1'], request.form['field2']
            book = Book(title=book_title, author=book_author, id=None)
            add_book_from_form(book)
            return "succesfully add book"
        else:
            return "error"
    else:
        return render_template('add_book.html')


@app.route('/books/author', methods=['GET', 'POST'])
def get_books_for_author():
    if request.method == "POST":
        if request.form:
            author = request.form["author"]
            books = get_books_from_author(author)
            return render_template('authors_books.html', books=books)
        else:
            return Response(status=404)
    else:
        return render_template("authors_books.html")

@app.route('/books/<id>', methods=['GET'])
def get_book(id: int):
    book = get_book_by_id(id)
    if book:
        update_book_count(book)
        return render_template("pred_index.html", book=book)
    else:
        return Response(status=418)


if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
