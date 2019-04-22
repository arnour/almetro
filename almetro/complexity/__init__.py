import math

class Notation:
    def __init__(self, fn, text=None, latex=None):
        """Provides a complexity notation.

        :param fn fn: A function that calculates the cost
        :param string text: Description label
        :param string latex: Description label compatible with latex notation
        """        
        self.__fn = fn
        self.__text = text        
        self.__latex = latex

    def text(self):
        return self.__latex if self.__latex else self.__text

    def fn(self):
        return self.__fn   
    
n_quadratic = Notation(lambda n: n**2, latex=r'$\mathcal{O}(n^2)$')
n_cubic = Notation(lambda n: n**3, latex=r'$\mathcal{O}(n^3)$')
n = Notation(lambda n: n, latex=r'$\mathcal{O}(n)$')
n_log_n = Notation(lambda n: n*math.log(n, 2), latex=r'$\mathcal{O}(n*\log{n})$')
log_n = Notation(lambda n: math.log(n, 2), latex=r'$\mathcal{O}(\log{n})$')