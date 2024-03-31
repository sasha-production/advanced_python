import logging
import logging.config
import string


class MyFilter(logging.Filter):
    # def __init__(self):
    #     super().__init__()
    @staticmethod
    def isascii(message):
        letters = string.ascii_letters
        return all([item in letters for item in message])

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.message
        return MyFilter.isascii(message)
# Словарь с конфигурацией


dict_config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': '%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s'
        },
    },
    'filters': {
        'isascii': {
            '()': MyFilter
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'brief',
            'stream': 'sys.stdout'
        },
        'file_handler': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
            'filename': 'calc_debug.log',
            'mode': 'w'
        },
    },
    'loggers': {
        'my_module': {
            'level': 'DEBUG',
            'handlers': ['file_handler']
        }
    }
}

