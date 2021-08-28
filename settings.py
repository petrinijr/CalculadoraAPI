import operator
import pathlib
import os

VALID_OPERATIONS = {
    'plus': operator.add,
    'minus': operator.sub,
    'divided': operator.truediv,
    'times': operator.mul
}

VALID_RANGE = range(100)

ROOT_DIR = pathlib.Path().resolve()

# app home urls
APP_1_HOME_URL = f"{os.environ['APP_1_HOST']}:{os.environ['APP_1_PORT']}"
APP_2_HOME_URL = f"{os.environ['APP_2_HOST']}:{os.environ['APP_2_PORT']}"
APP_3_HOME_URL = f"{os.environ['APP_3_HOST']}:{os.environ['APP_3_PORT']}"
