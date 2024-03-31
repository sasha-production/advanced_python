import logging
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
