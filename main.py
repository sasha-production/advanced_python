import os
import random
import re
from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
words = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')
counter = 0
@app.route('/')
def index():
    return '<h1>main_empty_page</h1>'

@app.route('/hello_world')
def hello_world_view():
    return f'<h1>Привет, мир!</h1>'


@app.route('/cars')
def cars_view():
    return f'<p>{", ".join(cars)}</p>'


@app.route('/cats')
def cats_view():
    choice = random.choice(cats)
    return f'<p>{choice}</p>'


@app.route('/get_time/now')
def get_time_now_view():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime('%H-%M-%S')
    return f'<p>Точное время: {current_time}</p>'


@app.route('/get_time/future')
def get_time_future_view():
    current_datetime = datetime.now()
    delta = timedelta(hours=1)
    future_datetime = current_datetime + delta
    future_time = future_datetime.strftime('%H-%M-%S')
    return f'<p>Точное время: {future_time}</p>'


def make_words():
    with open(BOOK_FILE, encoding='utf-8') as file:
        text = file.read()
        global words
        words = re.findall(r'\b[а-яА-Я]+\b', text)


@app.route('/get_random_word')
def get_random_word_view():
    if not words:
        make_words()
    word_random = random.choice(words)
    return f'<p>{word_random}</p>'


@app.route('/counter')
def counter():
    counter.visits += 1

    return f'<p>{counter.visits}</p>'


counter.visits = 0


if __name__ == '__main__':
    app.run(debug=True)