import time
import logging
from functools import wraps

def setup_custom_logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    logger = logging.getLogger(name)

    if (logger.hasHandlers()):
        logger.handlers.clear()

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.propagate = False

    return logger

def func_logger_detail(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return orig_func(*args, **kwargs)

    return wrapper

def func_logger(orig_func):

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f'Start {orig_func}')
        return orig_func(*args, **kwargs)

    return wrapper
def func_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = round(time.time() - t1, 1)
        print(f'{orig_func.__name__} ran in: {t2} sec')
        return result

    return wrapper

