import numpy as np
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
        """Provides a new instance of number sequence as a tuple.

        :returns: one number sequence. For example: (0.1, 0.3)
        :rtype: tuple(float)
        """
        length = int(self.size + (self.iterations * self.growth))
        self.iterations += 1        
        return np.array(random.sample(range(length * 2), length))
