import sys

from mod7 import utils
import logging

logger = logging.getLogger('my_logger')  # task 1
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter(fmt='%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)  # task 2

# обработчик для уровня debug
handler_debug = logging.FileHandler(filename='calc_debug.log', encoding='utf-8')
handler_debug.setLevel(level=logging.DEBUG)
handler_debug.setFormatter(fmt=formatter)
logger.addHandler(handler_debug)

# обработчик для уровня error
handler_error = logging.FileHandler(filename='calc_error.log', encoding='utf-8')
handler_error.setLevel(level=logging.ERROR)
handler_error.setFormatter(fmt=formatter)
logger.addHandler(handler_error)

handler.setFormatter(fmt=formatter)
logger.addHandler(handler)