
import math
from .kd_tree import *


class NearestNeighborIndex:
    """
    NearestNeighborIndex creates a k-d tree in 2 dimensions based on a list input of points.
    Constructing the tree is the slowest operation, so this is done in the class initializer.

    The nearest-neighbor calculation uses a basic k-NN search that evaluates leaves in the tree
    against their parents up to the root.

    A k-d tree was chosen due to my experience using (though not implementing) a k-NN search strategy
    for 3D point-on-screen calculations when determining which geometries to process during various
    rendering steps. Worst-case, it's as slow as the linear evaluation from find_nearest_slow [O(n)]
    but best-case is significantly faster.
    """

    def __init__(self, points):
        """
        takes an array of 2d tuples as input points to be indexed.
        """
        self.points = points

        # construct a k-d tree to search on
        self.tree = kdTree(points)

    @staticmethod
    def find_nearest_slow(query_point, haystack):
        """
        find_nearest_slow returns the point that is closest to query_point. If there are no indexed
        points, None is returned.
        """

        min_dist = None
        min_point = None

        for point in haystack:
            dist = math.sqrt(distance_sq(query_point, point))
            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_point = point

        return min_point

    @staticmethod
    def find_nearest_faster(query_point, points):
        """
        initial speed-up trick, check distance^2 instead of actually computing the distance.
        bigger deal on older machines and mostly depends on the implementation of sqrt;
        but found a 1.35% speed-up.
        """
        min_dist = None
        min_point = None

        for point in points:
            dist2 = distance_sq(query_point, point)
            if min_dist is None or dist2 < min_dist:
                min_dist = dist2
                min_point = point

        return min_point

    def find_nearest(self, query_point):
        """
        execute kd_nearest_neighbor for our k-d tree against query_point.

        only return the closest point, since that's all we care about.
        """
        [best, distance] = kd_nearest_neighbor(self.tree, query_point)
        return best
