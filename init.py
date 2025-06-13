import os
import sys
import shutil

if __name__ == '__main__':
    if not os.path.exists('catalog'):
        os.mkdir('catalog')

    if sys.argv.__len__() > 1:
        new_config = sys.argv[1]
        if os.path.exists(f'catalog\\{new_config}'):
            raise Exception(f'File {new_config} already exists')
        shutil.copy(f'templates\\config_template.py', f'catalog\\{new_config}.py')

        f = open('catalog\\__init__.py', 'a')
        f.write(f'from . import {new_config}\n')
        f.close()
