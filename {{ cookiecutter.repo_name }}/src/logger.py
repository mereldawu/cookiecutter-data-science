import time
import yaml
import logging
import logging.config
from functools import wraps

def get_logger():

    with open('src/logger_conf.yaml', 'rt') as f:
        logger_config = yaml.safe_load(f.read())
        logging.config.dictConfig(logger_config)
    logger = logging.getLogger(__name__)

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
        logging.info(f'Start')
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