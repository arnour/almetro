from matplotlib import pyplot as plt
from .spec import experimental_with_ratio_spec

class ChartLine:
    def __init__(self, data={}, label=None, color=None):
        self.data = data
        self.label = label
        self.color = color        
        self.plt_line = None

    def setup(self, plt_axis):
        self.plt_line = plt_axis.plot(self.data.keys(), self.data.values(), self.color, label=self.label)[0]

    @staticmethod
    def new(data={}, label=None, color=None):
        return ChartLine(data, label, color)


class ChartAxis:
    legend_loc = "upper left"
    grid = True

    def __init__(self, title=None, chart_lines=[], plt_axis=None):
        self.title = title         
        self.chart_lines = chart_lines
        self.plt_axis = plt_axis
    
    def setup(self): 
        for chart_line in self.chart_lines:
            chart_line.setup(self.plt_axis)
        self.plt_axis.set_title(self.title)
        self.plt_axis.grid(ChartAxis.grid)
        self.plt_axis.legend(loc=ChartAxis.legend_loc)
        self.plt_axis.label_outer()

    @staticmethod
    def new(title=None, chart_lines=[], plt_axis=None):
        return ChartAxis(title, chart_lines, plt_axis)

class Chart:
    def __init__(self, title=None, chart_axes=[], plt_figure=None):
        self.title = title
        self.chart_axes = chart_axes
        self.plt_figure = plt_figure
        
    def show(self):
        self.plt_figure.suptitle(self.title)
        for chart_axis in self.chart_axes:
            chart_axis.setup()

    @staticmethod
    def new(title=None, chart_axes=[], plt_figure=None):
        return Chart(title, chart_axes, plt_figure)

def build_chart(metro, complexity, spec_builder=experimental_with_ratio_spec):
    spec = spec_builder(metro, complexity)
    plt.close()
    fig, axes = plt.subplots(1, len(spec['axes']), sharex=True, sharey=True, figsize=(18, 10))
    chart_axes = []
    for i, axis_spec in enumerate(spec['axes']):
        chart_lines = []
        for line_spec in axis_spec['lines']:
            chart_lines.append(ChartLine.new(*line_spec))
        chart_axes.append(ChartAxis.new(axis_spec['title'], chart_lines, axes[i]))

    return Chart.new(spec['title'], chart_axes, fig)