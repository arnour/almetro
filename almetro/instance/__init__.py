import numpy as np

class Instance:

    def new(self):
        pass


class NumberSequence(Instance):

    def __init__(self, size=10, growth_rate=0.1, digits=0):
        """Provides a number sequence instance creator.

        :param int size: number of elements in the instance. Default is 10.
        :param int growth_rate: growth rate of instance size. Default is 0.1.
        :param int digits: number of decimal digits in each instance's element. Default is 0.
        """
        self.iterations = 0
        self.size = size
        self.growth = size * growth_rate
        self.digits = digits

    def new(self):
        """Provides a new instance of number sequence as a tuple.

        :returns: one number sequence. For example: (0.1, 0.3)
        :rtype: tuple(float)
        """
        length = int(self.size + (self.iterations * self.growth))
        self.iterations += 1        
        return np.around(np.random.random(length) * length, decimals=self.digits)
