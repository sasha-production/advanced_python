from flask import Flask

app = Flask(__name__)
cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']


@app.route('/')
def index():
    return '<h1>main_empty_page</h1>'

@app.route('/hello_world')
def hello_world_view():
    return f'<h1>Привет, мир!</h1>'


@app.route('/cars')
def cars_view():
    return f'<p>{", ".join(cars)}</p>'
@app.route('/some/')
def some():
    return '123'


@app.errorhandler(404)
def error_handler(error):
    base_url = 'http://localhost:5000'
    available_urls = [f'<a href={base_url+url.rule}>' + base_url + url.rule + '</a>' for url in app.url_map.iter_rules()][1:]
    return 'Page not found. Available pages<br>' + '<br>'.join(available_urls)


if __name__ == '__main__':
    app.run(debug=True)