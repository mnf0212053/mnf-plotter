import importlib
import sys
import os
import traceback

MAIN_DIR = f'{os.getcwd()}\\functions'
sys.path.append(MAIN_DIR)

import functions
try:
    from config import config
except ModuleNotFoundError:
    from templates.config_template import config


def filter_arg(_arg, _module):
    arg_split = _arg.split('-')
    if len(arg_split) == 1:
        return _arg == _module
    else:
        return arg_split[0] == _module

def get_config(_arg):
    arg_split = _arg.split('-')
    if len(arg_split) == 1:
        return config
    _config = arg_split[1]
    if not _config:
        raise Exception('Graph configuration not found.')
    return getattr(importlib.import_module('catalog'), _config)


if __name__ == '__main__':
    argv = sys.argv
    modules = list(filter(lambda d: len(d.split('__')) <= 1 and \
                                        (1 if len(argv) <= 1 else (d in list(map(lambda a: a.split('-')[0], argv[1:])))), dir(functions)))

    for module in modules:
        arg = list(filter(lambda a: filter_arg(a, module), sys.argv))

        obj = importlib.import_module(module)
        try:
            catalog_config = get_config(arg[0])
            conf = (catalog_config if catalog_config != config else config).config
        except Exception as err:
            print('Problem importing graph configuration:')
            print(traceback.format_exc())
            print('Currently using configuration config_template.py')
            conf = config

        plot = getattr(obj.main, list(filter(lambda o: o != 'Plotter', dir(obj.main)))[0])(**conf)
        plot.show_plot()
