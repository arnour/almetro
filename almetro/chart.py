from matplotlib import pyplot as plt

class ChartAxis:
    legend_loc = "upper left"
    def __init__(self, data, title, label, color, grid=True, line=None):
        self.data = data
        self.title = title
        self.label = label
        self.color = color        
        self.grid = grid   
        self.line = line
    
    def setup(self, axis):
        axis.set_title(self.title)
        axis.grid(self.grid)
        axis.legend(loc=ChartAxis.legend_loc)
        axis.label_outer()
        self.line = axis.plot(self.data.keys(), self.data.values(), self.color, label=self.label)[0]

    @staticmethod
    def new(data, title, label, color, grid=True, line=None):
        return ChartAxis(data, title, label, color, grid, line)

class Chart:
    def __init__(self, ratio, experimental, theoretical, complexity, elapsed_time):        
        self.ratio = ChartAxis.new(ratio, 'Ratio', 'c', 'tab:green')
        self.experimental = ChartAxis.new(experimental, 'Experimental', '$\mathcal{T}(\mathcal{f}(n))$', 'tab:blue')
        self.theoretical = ChartAxis.new(theoretical,'Theoretical', complexity.text(), 'tab:red')
        self.elapsed_time = elapsed_time
        
    def show(self):
        plt.close()
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharex=True, sharey=True)
        fig.suptitle('Approximate elapsed time {} in seconds'.format(self.elapsed_time))
        self.ratio.setup(ax1)
        self.experimental.setup(ax2)
        self.theoretical.setup(ax3)

    @staticmethod
    def new(ratio, experimental, theoretical, complexity, elapsed_time):
        return Chart(ratio, experimental, theoretical, complexity, elapsed_time)