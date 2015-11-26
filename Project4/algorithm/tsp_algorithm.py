from abc import ABCMeta, abstractmethod

__author__ = 'Don'


class TSPAlgorithm(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def solve(self, graph):
        pass
