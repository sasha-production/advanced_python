

from flask import Flask

app = Flask(__name__)


@app.route('/max_number/<path:line>')
def hello_world(line):
    res = all(map(lambda x: x.isdigit(), line.split('/')))
    if res:
        return f'макмальное число: {max([int(val) for val in line.split("/")])}'
    return 'передано не число'

if __name__ == '__main__':
    app.run(debug=True)