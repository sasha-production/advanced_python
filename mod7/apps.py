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


def show_list_of_commands() -> None:
    logger.info("Доступные команды:\n"
          "\"+\" - сложение\n"
          "\"-\" - вычитание\n"
          "\"*\" - умножение\n"
          "\"/\" - деление\n"
          "\"^\" - возведение в степень\n")


def get_command_from_user() -> str:
    command: str = input("Введите выражение с пробелами: ")
    return command


def process_command(command: str) -> tuple[float, float, str] | None:
    command_split: [str] = command.split()
    if len(command_split) != 3:
        return None
    number_1 = float(command_split[0])
    number_2 = float(command_split[2])
    operation = command_split[1]
    return number_1, number_2, operation


def get_result(command: tuple[float, float, str] | None) -> str:
    if command is None:
        logger.error('некорректная строка')
        return "Вы ввели не корректную строку, повторите попытку."
    number_1, number_2, operation = command
    result: float = utils.calculate(number_1, number_2, operation)
    return str(result)


def give_result_to_user(result: str) -> None:
    logger.debug(result)


if __name__ == '__main__':
    show_list_of_commands()
    while True:
        command: str = get_command_from_user()
        processed_command = process_command(command)
        result: str = get_result(processed_command)
        give_result_to_user(result)
