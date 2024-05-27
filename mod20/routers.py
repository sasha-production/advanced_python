from flask import Flask, jsonify, request
from mod20.models import Base, engine, session, Book, Student, ReceivingBook
from datetime import datetime
from sqlalchemy import update

app = Flask(__name__)


@app.before_request
def before_request_func():
    Base.metadata.create_all(engine)


@app.route('/books', methods=['GET', ])
def get_books():
    books = session.query(Book).all()
    books_list = [book.to_json() for book in books]
    return books_list


@app.route('/take_book', methods=['GET', 'POST'])
def take_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        date_of_return = datetime.strptime(request.form.get('date_of_return'), '%Y-%m-%d')
        new_take_book = ReceivingBook(book_id=book_id, student_id=student_id, date_of_return=date_of_return)
        session.add(new_take_book)
        book = session.query(Book).filter(Book.id == book_id).one_or_none()
        session.execute(update(Book).filter(Book.id == book_id).values(count=book.count - 1))
        session.commit()
        session.close()
    return "Вы взяли книгу", 201


@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        book_id = request.form.get('book_id', type=int)
        student_id = request.form.get('student_id', type=int)
        query = session.query(ReceivingBook).filter(
            ReceivingBook.book_id == book_id and ReceivingBook.student_id == student_id
        ).one_or_none()
        if query:
            book = session.query(Book).filter(Book.id == book_id).one_or_none()
            session.execute(update(Book).filter(Book.id == book_id).values(count=book.count + 1))
            session.query(ReceivingBook).filter(ReceivingBook.id == query.id).delete()
            session.commit()
            session.close()
            return jsonify({"message": "Book returned successfully"})
        else:
            session.close()
            return jsonify({"error": "No such record found"})


@app.route('/debtors', methods=['GET', ])
def get_debtors():
    debts = session.query(ReceivingBook).all()
    debts_list = []
    for debt in debts:
        if debt.count_date_with_book > 14:
            student = session.query(Student).filter(Student.id == debt.student_id).one_or_none()
            debts_list.append(student.to_json())
    session.close()
    return jsonify(debts_list=debts_list), 200


if __name__ == '__main__':
    app.run()