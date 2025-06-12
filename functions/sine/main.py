import numpy as np
from matplotlib import pyplot

from tools.plotter.plotter import Plotter


class SinePlotter(Plotter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sine = kwargs.get('sine', {})
        frequency = sine.get('frequency', {})
        phase_difference = sine.get('phase_difference', {})
        self.frequency = frequency.get('normal', 1)
        self.angular_frequency = frequency.get('angular', 1)
        self.use_angular_frequency = frequency.get('use_angular', False)
        self.amplitude = sine.get('amplitude', 1)
        self.phase_difference_radian = phase_difference.get('radian', np.pi / 2)
        self.phase_difference_degree = phase_difference.get('degree', 90)
        self.use_degree = phase_difference.get('use_degree', False)

    def function(self):
        time = np.linspace(
            self._kwargs.get('min', 0),
            self._kwargs.get('max', np.pi),
            num=self._kwargs.get('count', 1000)
        )
        frequency = self.angular_frequency if self.use_angular_frequency else 2 * np.pi * self.frequency
        phase_difference = ((self.phase_difference_degree / 180) * np.pi) if self.use_degree else self.phase_difference_radian
        return time, self.amplitude * np.sin(frequency * time + phase_difference)

    def set_label(self):
        pyplot.xlabel('t')
        pyplot.ylabel('y')