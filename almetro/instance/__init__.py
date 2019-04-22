import random

class InstanceProvider:

    def __init__(self, fn=None):
        """Provides a static instance creator.

        :param fn fn: A function that returns the instance
        """    
        self.fn = fn
        
    def new(self):
        """Provides a new instance value from fn.

        :returns: any type of instance
        """
        return self.fn()

    @staticmethod
    def function(function=None):
        return InstanceProvider(function)
    
    @staticmethod
    def growing(size=10, growth_rate=0.1):
        return GrowingNumberSequenceProvider(size=size, growth_rate=growth_rate)


class GrowingNumberSequenceProvider(InstanceProvider):

    def __init__(self, size=10, growth_rate=0.1):
        """Provides a growing int sequence without repetition instance creator.

        :param int size: number of elements in the instance. Default is 10.
        :param int growth_rate: growth rate of instance size. Default is 0.1 (10%).
        """
        self.iterations = 0
        self.size = size
        self.growth = size * growth_rate

    def new(self):
        """Provides a new int list as an instance.

        :returns: one int list. For example: [1, 3]
        :rtype: list(int)
        """
        length = int(self.size + (self.iterations * self.growth))
        self.iterations += 1        
        return random.sample(range(length * 2), length)
