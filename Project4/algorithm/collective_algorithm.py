from algorithm.tsp_algorithm import TSPAlgorithm


class RealTSPAlgorithm(TSPAlgorithm):
    def __init__(self):
        TSPAlgorithm.__init__(self)

    def solve(self, graph):
        return {
            'total': 2,
            'order': [0, 1]
        }
