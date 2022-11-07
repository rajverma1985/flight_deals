import logging.config
import logging

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('rotating_logger')


def add(x, y):
    logger.info("added {} and {}".format(x, y))
    return x + y


def multiply(x, y):
    logger.info("multiplied {} and {}".format(x, y))
    return x * y


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("error occurred")
    else:
        logger.info("divided {}/{} the result is {}".format(x, y, result))
        return result


for _ in range(10000):
    divide(1, 2)
