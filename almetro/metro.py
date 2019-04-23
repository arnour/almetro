from .chart import Chart
from .complexity import cn
import timeit

class Metro:
    def __init__(self):
        self.__start = timeit.default_timer()
        self.elapsed_time = 0
        self.experimental = {}

    def register(self, instance, timestats):
        self.elapsed_time = timeit.default_timer() - self.__start
        self.experimental[len(instance)] = min(timestats)

    def chart(self, complexity=cn):
        if not complexity:
            raise TypeError('complexity must be provided')     
        theoretical = {}
        ratio = {}
        for n, t_fn in self.experimental.items():
            theoretical[n] = complexity.fn()(n)
            ratio[n] = t_fn/max(theoretical[n], 0.1)
        return Chart.new(ratio=ratio, experimental=self.experimental, theoretical=theoretical, complexity=complexity, elapsed_time=self.elapsed_time)

    @staticmethod
    def new():
        return Metro()