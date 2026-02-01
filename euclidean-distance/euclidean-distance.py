import numpy as np
from scipy.spatial import distance


def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    return distance.euclidean(x, y)

