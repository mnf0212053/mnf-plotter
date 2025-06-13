import numpy as np

config = {
    'plot_config': {
        'color': 'black',
        'linestyle': '-'
    },
    'x_line': {
        'enabled': True,
        'config': {
            'color': 'black',
            'linestyle': '--',
            'linewidth': 0.5
        },
    },
    'y_line': {
        'enabled': True,
        'config': {
            'color': 'black',
            'linestyle': '--',
            'linewidth': 0.5
        },
    },
    'sine': {
        'frequency': {
            'normal': 2,
            'angular': 2,
            'use_angular': True
        },
        'amplitude': 1,
        'phase_difference': {
            'radian': np.pi / 4,
            'degree': 90,
            'use_degree': False
        }
    },
    'lissajous': {
        'function1': lambda t: 3 * np.cos(t),
        'function2': lambda t: 3 * np.sin(t),
        'phase1': {
            'radian': np.pi / 2,
            'degree': 60,
            'use_degree': False
        },
        'phase2': {
            'radian': np.pi / 4,
            'degree': 60,
            'use_degree': False
        },
        'phase_difference': {
            'radian': np.pi / 4,
            'degree': 10,
            'use_degree': True
        },
        'use_phase_difference': True,
    },
    'min': -np.pi,
    'max': np.pi,
    'count': 1000
}