import logging
import math

from task1_apps import logger
# logger = logging.getLogger('utils_logger')
# logging.basicConfig(level=logging.DEBUG)


def calculate(a: float, b: float, operation: str) -> float:
    logger.debug('сопоставление операции')
    match operation:
        case "+":
            return _addition(a, b)
        case "-":
            return _subtraction(a, b)
        case "*":
            return _multiplication(a, b)
        case "/":
            return _division(a, b)
        case "^":
            return _pow(a, b)


def _addition(a: float, b: float) -> float:
    result: float = a + b
    return result


def _subtraction(a: float, b: float) -> float:
    result: float = a - b
    return result


def _multiplication(a: float, b: float) -> float:
    result: float = a * b
    return result


def _division(a: float, b: float) -> float:
    result: float = a / b
    return result


def _pow(a: float, b: float) -> float:
    result: float = math.pow(a, b)
    return result