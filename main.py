import importlib
import sys
MAIN_DIR = 'C:\\Users\\mnurf\\Documents\\Projects\\python-projects\\custom-plotter\\functions'
sys.path.append(MAIN_DIR)

import functions
try:
    from config import config
except ModuleNotFoundError:
    from config_template import config
from tools.plotter.plotter import Plotter


if __name__ == '__main__':
    argv = sys.argv
    modules = list(filter(lambda d: len(d.split('__')) <= 1 and \
                                        (1 if len(argv) <= 1 else (d in argv[1:])), dir(functions)))

    for module in modules:
        obj = importlib.import_module(module)
        plot = getattr(obj.main, list(filter(lambda o: o != 'Plotter', dir(obj.main)))[0])(**config)
        plot.show_plot()
