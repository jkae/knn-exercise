
import math
from pprint import pformat

#################################################################################################################
# Barebones k-d tree and k-NN search implementation.
# Only *actually* supports 2 dimensions. Not self-balancing and doesn't actually implement a balancing algorithm.
#################################################################################################################

class kdTreeNode:
    def __init__(self, location: tuple[float, float], left = None, right = None):
        self.location = location
        self.children = [left, right]

    def __repr__(self):
        return pformat((self.location, self.children))


def kdTree(points: list, depth: int = 0, k: int = 2):
    """
    generate a k-d tree from a list of points.

    accepts input:
    - points: the list of points
    - depth: the current tree depth; should always be 0 if executed manually
    - k: the dimensionality of the tree; only 2 is supported
    """

    # this constructor was taken from the k-d tree page on Wikipedia but was implemented from the
    # English description; the Python implementation example was not referenced.

    if (not points or len(points) == 0):
        return None

    axis: int = depth % k
    points.sort(key = lambda e : e[axis])

    count = len(points)
    if (count == 1):
        return kdTreeNode(points[0])

    mid = count // 2
    return kdTreeNode(points[mid], kdTree(points[:mid], depth + 1), kdTree(points[mid+1:], depth + 1))


def kd_nearest_neighbor(root: kdTreeNode, to_check: tuple[float, float], depth: int = 0, k: int = 2):
    """
    find the nearest neighbor, within a k-d tree, to a given point.

    accepts input:
    - root: the k-d tree's root node; or the node you'd like to start from. recursively traces all nodes.
    - to_check: the point to check; restricted to a 2-D tuple of floats
    - depth: the current tree depth; should always be 0 if executed manually
    - k: the dimensionality of the tree; only 2 is supported

    returns a list composed of the nearest neighbor and that neighbor's distance from the input point.
    if nothing is found, returns None.
    """

    # this algorithm was implemented following the English description on Wikipedia.

    if (not root or not to_check):
        return [None, None]

    # determine axis to search same way we filled the tree & find the current dist2
    axis: int = depth % k

    current_best = root.location
    current_best_distance = distance_sq(to_check, root.location)

    # scan our branches
    child = 0 if to_check[axis] < root.location[axis] else 1
    [leaf, leaf_distance] = kd_nearest_neighbor(root.children[child], to_check, depth + 1)

    # determine if the leaf distance was better than our current position
    if (leaf and leaf_distance < current_best_distance):
        current_best = leaf
        current_best_distance = leaf_distance

    # check if the distance to the current position, on a single axis, is better than the current best distance
    if (abs(root.location[axis] - to_check[axis]) < math.sqrt(current_best_distance)):
        # if it is, we should check the other node -- abs(child-1) will flip between 0 and 1 :)
        [leaf, leaf_distance] = kd_nearest_neighbor(root.children[abs(child-1)], to_check, depth + 1)
        if (leaf and leaf_distance < current_best_distance):
            current_best = leaf
            current_best_distance = leaf_distance

    return [current_best, current_best_distance]


def distance_sq(a: tuple[float, float], b: tuple[float, float]):
    """
    determine the square distance between two 2D points.
    """

    deltax = b[0] - a[0]
    deltay = b[1] - a[1]
    return deltax * deltax + deltay * deltay
