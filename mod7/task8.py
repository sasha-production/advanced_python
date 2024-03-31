import logging.config
import logging
import logging.handlers
import flask
from flask import request

from task4.make_dict_config import dict_config


app = flask.Flask(__name__)

logger = logging.getLogger('my_logger')
logging.config.dictConfig(dict_config)

http_handler = logging.handlers.HTTPHandler(host='localhost:5000', url='/get/')
logger.addHandler(http_handler)

http_handler_post = logging.handlers.HTTPHandler('localhost:5000', '/log', method='POST')
logger.addHandler(http_handler)
@app.route('/get/', methods=['GET'])
def send_logs():
    log_data = request.args.to_dict()
    # Обработка принятого лога
    print(log_data)
    return 'Log received', 200

@app.route('/send/', methpds='[POST]')
def send():
    log_data = request.get_json()
    # Обработка принятого лога
    print(log_data)
    return 'Log received', 200

if __name__ == '__main__':
    app.run(debug=True)