import random

class Instance:

    def get(self):
        pass


class NumberSequence(Instance):

    def __init__(self, size=10, digits=0):
        """Provides a number sequence instance creator.

        :param int size: number of elements in the instance. Default is 10.
        :param int digits: number of decimal digits in each instance's element. Default is 0.
        """
        self.value = tuple(round(random.random() * size, digits) for i in range(0, size))

    def get(self):
        """Provides an instance as the form of a number sequence for a simulation.

        :returns: a number sequence. For example: ((0.1, 0.3), (0.4, 0.5))
        :rtype: tuple(tuple(float))
        """
        return self.value
