from math import sqrt


class GraphParser:
    def __init__(self):
        pass

    def parse_input(self, input_string):
        pass

    def format_output(self, solution):
        pass

    def get_distance(self, v1, v2):

        (v1x, v1y) = v1
        (v2x, v2y) = v2

        return round(sqrt(pow(abs(v2y - v1y), 2) + pow(abs(v2x - v1x), 2)))