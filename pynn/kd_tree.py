
import math

####################################################
# Barebones k-d tree and k-NN search implementation.
#
# Only *actually* supports 2 dimensions.
####################################################

class kdTreeNode:
    def __init__(self, location: tuple[float, float], left = None, right = None):
        self.location = location
        self.children = [left, right]


def kdTree(points: list, depth: int = 0, k: int = 2):
    """
    generate a k-d tree from a list of points.
    this constructor was taken from the k-d tree page on Wikipedia but was implemented from the
    English description; the Python implementation example was not referenced.
    """
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
    this algorithm was implemented following the English description on Wikipedia.
    """
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
    get the square distance between two points.
    """
    deltax = b[0] - a[0]
    deltay = b[1] - a[1]
    return deltax * deltax + deltay * deltay
