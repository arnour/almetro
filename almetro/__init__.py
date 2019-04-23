from almetro.instance import InstanceProvider
from matplotlib import pyplot as plt
import timeit
import copy

class Metro:
    def __init__(self, complexity=None):
        self.__complexity = complexity
        self.__stats = {}
        self.__reference_stats = {}

    def register(self, instance, timestats):
        instance_size = len(instance)
        instance_cost = min(timestats)
        self.__stats[instance_size] = instance_cost
        if self.__complexity:
            self.__reference_stats[instance_size] = self.__complexity.fn()(instance_size)

    def stats(self):
        return copy.deepcopy(self.__stats)

    def reference_stats(self):
        return copy.deepcopy(self.__reference_stats)

    def complexity(self):
        return copy.deepcopy(self.__complexity)        

    def plot(self):
        return Plot(self)


class Al:
    def __init__(self, iterations=10, repeat=10, instance_provider=InstanceProvider()):
        self.iterations = iterations
        self.repeat = repeat
        self.instance_provider = instance_provider

    def metro(self, algorithm, complexity=None):
        metro = Metro(complexity)
        for _ in range(self.iterations):
            instance = self.instance_provider.new()

            def runner():
                algorithm(instance)
            metro.register(instance, timeit.repeat(runner, number=10, repeat=self.repeat))
        return metro

class Plot:

    def __init__(self, metro):        
        self.__metro = metro
        self.algorithm_line = None
        self.theoretical_line = None
    
    def __algorithm(self, data):
        plt.subplot(1, 2, 1).set_title("Algorithm")
        plt.ylabel('time (s)')
        plt.xlabel('instance size')
        plt.grid(True)        
        self.algorithm_line = plt.plot(data.keys(), data.values(), 'g--', label='Your algorithm')[0]
        plt.legend(loc="upper left")
    
    def __theoretical(self, data):
        plt.subplot(1, 2, 2).set_title("Theoretical")
        plt.xticks([])
        plt.yticks([])
        plt.grid(True)        
        self.theoretical_line = plt.plot(data.keys(), data.values(), 'b--', label=self.__metro.complexity().text())[0]
        plt.legend(loc="upper left")

    def show(self):
        plt.close()
        self.__algorithm(self.__metro.stats())
        self.__theoretical(self.__metro.reference_stats())   
        plt.tight_layout()     
