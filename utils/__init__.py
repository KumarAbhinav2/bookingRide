from math import sqrt

def getEuclideanDistance(fromLoc, toLoc):
    x = fromLoc.getLatLon()
    y = toLoc.getLatLon()
    return sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))