from matplotlib import pyplot
import numpy as np


class Plotter:
    def __init__(self, **kwargs):
        fig = kwargs.get('fig', pyplot.figure())
        self.fig = fig
        self.ax = self.fig.add_subplot(111)
        self._kwargs = kwargs
        self._plot_config = kwargs.get('plot_config', {})

    def function(self):
        phase = self._kwargs.get('phase', np.linspace(0, 2*np.pi, 100))
        return phase, np.sin(2*np.pi*phase)

    def generate_pyplot(self):
        x, y = self.function()
        return self.ax.plot(x, y, **self._plot_config)

    def set_label(self):
        pyplot.xlabel('x')
        pyplot.ylabel('y')

    def show_plot(self):
        pyplt = self.generate_pyplot()
        x_line = self._kwargs.get('x_line', {})
        y_line = self._kwargs.get('y_line', {})
        if x_line.get('enabled', True):
            self.ax.plot([
                self._kwargs.get('min', 0),
                self._kwargs.get('max', 10)
            ], [0, 0], **x_line.get('config', {}))
        if y_line.get('enabled', True):
            self.ax.plot([0, 0], [
                self._kwargs.get('min', 0),
                self._kwargs.get('max', 10)
            ], [0, 0], **y_line.get('config', {}))
        self.set_label()
        pyplot.show()
