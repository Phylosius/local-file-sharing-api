import os

import environ

env = environ.Env()
environ.Env.read_env()

FILE_STOCKAGE_PATH = env('FILE_STOCKAGE_PATH')


def get_stockage_path():
    return FILE_STOCKAGE_PATH


def is_file_exist(file_name):

    try:
        with open(get_stockage_path() + file_name, 'r') as f:
            if f.read():
                return True
    except FileNotFoundError:
        return False


def save_file(file_name, data):

    with open(get_stockage_path() + file_name, 'wb') as f:
        f.write(data)
        f.close()
        return True


def get_file_content(file_name):

    with open(get_stockage_path() + file_name, 'rb') as f:
        return f.read()


def delete_file(file_name):

    os.remove(get_stockage_path() + file_name)
