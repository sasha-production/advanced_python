from flask import Flask
from datetime import datetime

app = Flask(__name__)
weekdays_tuple = ('понедельника', 'вторника', 'среды', 'четверга', 'пятницы', 'субботы', 'воскресенья')


@app.route('/hello-world/<name>')
def hello_world(name):
    weekday_number = datetime.today().weekday()
    weekday = weekdays_tuple[weekday_number]
    word_good = 'Хорошего' if weekday_number in (0, 1, 3,6) else 'Хорошей'
    return f"Привет, {name}. {word_good} {weekday}!"

if __name__ == '__main__':
    app.run(debug=True)