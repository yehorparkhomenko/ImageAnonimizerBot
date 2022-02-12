import os
import uuid


def gen_filepath(dir_path: str, ext: str) -> str:
    if not dir_path.endswith(os.path.sep):
        dir_path = dir_path + os.path.sep

    if not ext.startswith('.'):
        ext = '.' + ext

    while True:
        filename = dir_path + str(uuid.uuid4()) + ext
        if not os.path.exists(dir_path) or not os.path.isfile(filename):
            return filename

