import json
import logging

class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return (None, kwargs) if '"' in msg or "'" in msg else (msg, kwargs)


logger = JsonAdapter(logging.getLogger(__name__))
dict_format = {'time': '%(asctime)s',
               'level': '%(levelname)s',
               'message': '%(message)s'}
json_str = json.dumps(dict_format)
logging.basicConfig(filename='skillbox_json_messages.log', format=json_str, datefmt='%H:%M:%S')
logger.info('Сообщение')
logger.warning('Message')
