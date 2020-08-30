from math import sqrt

def getEuclideanDistance(x, y):
    return sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))