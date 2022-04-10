# FILE_TYPES includes submenu's name and the file repo lacation
FILE_TYPES = {
    'software': r'd:\software',
    'document': r'd:\document'
}
# release mode will disable log
RUN_MODE = 'release'
import os

LOG_FILE_LOCATION = f'{os.path.dirname(os.path.realpath(__file__))}\\sort-it.log'
