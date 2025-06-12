import numpy as np

from tools.plotter.plotter import Plotter


class LinearPlotter(Plotter):
    def __init__(self, **kwargs):
        kwargs.update({
            'color': 'black'
        })
        super().__init__(**kwargs)
        self.constant = 5

    def function(self):
        phase = self._kwargs.get('phase', np.linspace(0, 2*np.pi, 100))
        constant = self._kwargs.get('constant', self.constant)
        return phase, constant*phase
