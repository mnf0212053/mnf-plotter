import numpy as np
from matplotlib import pyplot

from tools.plotter.plotter import Plotter


class LissajousPlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lissajous = kwargs.get('lissajous', {})
        phase1 = lissajous.get('phase1', {})
        phase2 = lissajous.get('phase2', {})

        if not lissajous.get('use_phase_difference', False):
            self.phase1 = phase1.get('radian', 0) if not phase1.get('use_degree', False) else phase1.get('degree', 0)/180 * np.pi
            self.phase2 = phase2.get('radian', np.pi/4) if not phase2.get('use_degree', False) else phase2.get('degree', 45)/180 * np.pi
        else:
            phase_difference = lissajous.get('phase_difference', {})
            self.phase1 = 0
            self.phase2 = phase_difference.get('radian', 0) if not phase_difference.get('use_degree', False) else phase_difference.get('degree', 0)/180 * np.pi

        self.function1 = lissajous.get('function1', lambda t: 3 * np.sin(t))
        self.function2 = lissajous.get('function2', lambda t: 3 * np.cos(t))

    def function(self):
        time = np.linspace(0, 2*np.pi, 100)
        return self.function1(time + self.phase1), self.function2(time + self.phase2)
