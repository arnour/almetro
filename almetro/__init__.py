from almetro.instance import Instance
import numpy as np
import timeit


class Metro:
    __stats_dtype = [('n', 'i8',), ('cost', 'f8',)]
    def __init__(self):
        self.__stats = {}

    def register(self, instance, timestats):
        self.__stats[len(instance)] = min(timestats)

    def stats(self):
        return np.array(list(self.__stats.items()), dtype=self.__stats_dtype)


class Al:
    def __init__(self, iterations=10, repeat=1, instance_provider=Instance()):
        self.iterations = iterations
        self.repeat = repeat
        self.instance_provider = instance_provider

    def metro(self, algorithm):
        metro = Metro()
        for i in range(self.iterations):
            instance = self.instance_provider.new()

            def runner():
                algorithm(instance)
            metro.register(instance, timeit.repeat(runner, number=1, repeat=self.repeat))
        return metro
