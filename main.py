from config import *
from context_menu import menus
import shutil
from pathlib import Path
import datetime
import os


class TypeEnum:
    FILES = 'FILES'
    DIRECTORY = 'DIRECTORY'
    DIRECTORY_BACKGROUND = 'DIRECTORY_BACKGROUND'
    DRIVE = 'DRIVE'


def sort_it_log(level, msg):
    if RUN_MODE == 'release':
        return
    with open(LOG_FILE_LOCATION, 'a', encoding='utf-8') as log_file:
        log_file.write(f'{datetime.datetime.now()}\t[{level}]: {msg}\n')


def sort_file(filename, params):
    """
    move file to a certain directory
    """
    # check if dest path is exists
    params = os.path.join(params, f'{datetime.datetime.today().strftime("%Y-%m")}')
    sort_it_log('INFO', f'params: {params}')
    Path(params).mkdir(parents=True, exist_ok=True)
    for f in filename:
        pure_filename = f.split('\\')[-1]
        destination = os.path.join(params, pure_filename)
        if SORTING_STRATEGY == 'move':
            shutil.move(f, destination)
        else:
            shutil.copy(f, destination)
        sort_it_log('INFO', f'selected file\'s name: {pure_filename}')
        sort_it_log('INFO', f'destination: {destination}')


def set_context_command(name, path) -> menus.ContextCommand:
    return menus.ContextCommand(name=name, python=sort_file, params=path)


def install():
    cm = menus.ContextMenu(name='Sort it!', type=TypeEnum.FILES)
    context_command_list = [set_context_command(k, v) for k, v in FILE_TYPES.items()]
    cm.add_items(context_command_list)
    cm.compile()


def uninstall():
    menus.removeMenu('Sort it!', type='FILES')


def reinstall():
    try:
        uninstall()
    except FileNotFoundError:
        pass
    finally:
        install()


if __name__ == '__main__':
    reinstall()
