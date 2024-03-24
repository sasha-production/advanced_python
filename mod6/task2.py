import getpass
import hashlib
import logging
import re
logger = logging.getLogger(__name__)


def binary_search(password_piece: str) -> str:
    '''
    search password_piece in file
    '''
    with open('words.txt', encoding='utf-8') as file:
        words = file.readlines()
        left, right = 0, len(words)
        logger.debug(f"Старт бинарного поиска")
        while right - left > 0:
            mid = (left + right) // 2
            if password_piece < words[mid]:
                right = mid
            else:
                left = mid + 1
        return words[right].strip()


def is_strong_password(password: str) -> bool:
    '''checking password, if piece of password was found in file - return True,
    else - return None'''
    logger.debug("Проверка пароля на сложность")
    password = password.lower()
    words_in_password = re.findall(r'[a-zA-Z]{4,}', password)
    for word in words_in_password:
        logger.debug(f"Поиск {word} в файле слов")
        res_of_search = binary_search(word)
        if res_of_search == word:
            logger.warning(f"Пароль содержит слово английского языка: {res_of_search}")
            return True


def input_and_check_password() -> bool:
    logger.debug("Начало input_and_check_password")
    password: str = getpass.getpass()

    if not password:
        logger.warning("Вы ввели пустой пароль.")
        return False
    if is_strong_password(password):
        logger.warning("Введен слабый пароль")
        return False

    try:
        hasher = hashlib.md5()

        hasher.update(password.encode("latin-1"))

        if hasher.hexdigest() == "098f6bcd4621d373cade4e832627b4f6":
            return True
    except ValueError as ex:
        logger.exception("Вы ввели некорректный символ ", exc_info=ex)

    return False


if __name__ == '__main__':
    logging.basicConfig(filename='stderr.txt', filemode='w', encoding='utf-8', level=logging.DEBUG, datefmt="%H:%M:%S", format='%(asctime)s - %(levelname)s - %(message)s')
    logger.info("Вы пытаетесь аутентифицироваться в Skillbox")
    count_number: int = 3
    logger.info(f"У вас есть {count_number} попыток")

    while count_number > 0:
        if input_and_check_password():
            exit(0)
        count_number -= 1

    logger.error("Пользователь трижды ввёл не правильный пароль!")
    exit(1)