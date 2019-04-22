from almetro.instance import InstanceProvider
from matplotlib import pyplot as plt
import almetro.complexity as complexity
import timeit
import copy


class Metro:
    def __init__(self, complexity=complexity.n):
        self.__complexity = complexity
        self.__stats = {}
        self.__reference_stats = {}

    def register(self, instance, timestats):
        instance_size = len(instance)
        self.__stats[instance_size] = min(timestats)
        self.__reference_stats[instance_size] = int(self.__complexity.fn()(instance_size))

    def stats(self):
        return copy.deepcopy(self.__stats)

    def reference_stats(self):
        return copy.deepcopy(self.__reference_stats)        

    def plot(self):     
        plt.title('Complexity algorithm comparison')
        plt.ylabel('time')
        plt.xlabel('size')
        plt.grid(True)          
        plt.legend()
        plt.plot(self.reference_stats().keys(), self.reference_stats().items(), label=self.__complexity.text)        
        return plt.plot(self.stats().keys(), self.stats().items(), label='your algorithm')




class Al:
    def __init__(self, iterations=10, repeat=1, instance_provider=InstanceProvider()):
        self.iterations = iterations
        self.repeat = repeat
        self.instance_provider = instance_provider

    def metro(self, algorithm, complexity=complexity.n):
        metro = Metro(complexity=complexity)
        for _ in range(self.iterations):
            instance = self.instance_provider.new()

            def runner():
                algorithm(instance)
            metro.register(instance, timeit.repeat(runner, number=1, repeat=self.repeat))
        return metro
