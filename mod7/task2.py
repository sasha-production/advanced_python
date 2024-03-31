import sys

from mod7 import utils
import logging

logger = logging.getLogger('my_logger')  # task 1
logger.setLevel(level=logging.DEBUG)

formatter = logging.Formatter(fmt='%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s')
handler = logging.StreamHandler(stream=sys.stdout)  # task 2

handler.setFormatter(fmt=formatter)
logger.addHandler(handler)