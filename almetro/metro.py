import almetro.chart as chart
from almetro.complexity import cn
import timeit

class Metro:
    def __init__(self):
        self.__start = timeit.default_timer()
        self.elapsed_time = 0
        self.experimental = {}
        self.theoretical = {}
        self.ratio = {}

    def register(self, instance, timestats):
        self.elapsed_time = timeit.default_timer() - self.__start
        self.experimental[len(instance)] = min(timestats)

    def chart(self, complexity=cn):
        if not complexity:
            raise TypeError('complexity must be provided')     
        self.theoretical = {}
        self.ratio = {}
        for n, t_fn in self.experimental.items():
            self.theoretical[n] = complexity.fn()(n)
            self.ratio[n] = t_fn/max(self.theoretical[n], 0.1)
        return chart.build_chart(self, complexity)

    @staticmethod
    def new():
        return Metro()