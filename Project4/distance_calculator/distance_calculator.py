from math import sqrt


def get_distance(v1, v2):
    (v1x, v1y) = v1
    (v2x, v2y) = v2
    return round(sqrt(pow(abs(v2y - v1y), 2) + pow(abs(v2x - v1x), 2)))
