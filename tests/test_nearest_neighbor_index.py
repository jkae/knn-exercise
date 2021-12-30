"""nn_search_test"""

import random
import time
import unittest

from pynn import NearestNeighborIndex


class NearestNeighborIndexTest(unittest.TestCase):

    def test_basic(self):
        """
        test_basic tests a handful of nearest neighbor queries to make sure they return the right
        result.
        """

        test_points = [
            (1, 2),
            (1, 0),
            (10, 5),
            (-1000, 20),
            (3.14159, 42),
            (42, 3.14159),
        ]

        uut = NearestNeighborIndex(test_points)

        self.assertEqual((1, 0), uut.find_nearest((0, 0)))
        self.assertEqual((-1000, 20), uut.find_nearest((-2000, 0)))
        self.assertEqual((42, 3.14159), uut.find_nearest((40, 3)))


    def test_single(self):
        """
        test_single tests against a k-d tree composed of one node to verify only it will be returned
        """

        test_points = [
            (42, 3.14159),
        ]

        uut = NearestNeighborIndex(test_points)

        self.assertEqual((42, 3.14159), uut.find_nearest((0, 0)))
        self.assertEqual((42, 3.14159), uut.find_nearest((-2000, 0)))
        self.assertEqual((42, 3.14159), uut.find_nearest((40, 3)))


    def test_3d(self):
        """
        test_3d tests that our implementation shouldn't break if we use multiple dimensions for points,
        but since the tree is 2D it won't really work

        Changes:
        - update distance_sq to take arbitrary dimension count
        - update NearestNeighborIndex.__init__ to take dimension count
        - update NearestNeighborIndex.find_nearest to determine input dimension count and use that as input to kd_nearest_neighbor
        - handle if the dimensionality of the tree is different to the input
        """

        test_points = [
            (1, 2, 0),
            (1, 0, -10),
            (10, 5, 30),
            (-1000, 20, 2000),
            (3.14159, 42, -5000),
            (42, 3.14159, -0.005),
        ]

        uut = NearestNeighborIndex(test_points)

        self.assertEqual((1, 0, -10), uut.find_nearest((0, 0)))
        self.assertEqual((-1000, 20, 2000), uut.find_nearest((-2000, 0)))
        self.assertEqual((42, 3.14159, -0.005), uut.find_nearest((40, 3)))


    def test_no_query(self):
        """
        test_no_query verifies that our implementation doesn't fail if we attempt to find the
        nearest point to None
        """

        test_points = [
            (1, 2, 0),
            (1, 0, -10),
            (10, 5, 30),
            (-1000, 20, 2000),
            (3.14159, 42, -5000),
            (42, 3.14159, -0.005),
        ]
        uut = NearestNeighborIndex(test_points)
        self.assertEqual(None, uut.find_nearest(None))


    def test_no_points(self):
        """
        test_no_points verifies that our implementation doesn't fail if
        - we attempt to find the nearest value to a point in an empty tree
        - we attempt to find the nearest value to nothing in an empty tree
        """

        emptyArray = NearestNeighborIndex([])
        none = NearestNeighborIndex(None)

        self.assertEqual(None, emptyArray.find_nearest(None))
        self.assertEqual(None, none.find_nearest(None))
        
        self.assertEqual(None, emptyArray.find_nearest((1, 3)))
        self.assertEqual(None, none.find_nearest((1, 3)))


    def test_benchmark(self):
        """
        test_benchmark tests a bunch of values using the slow and fast version of the index
        to determine the effective speedup.
        """

        def rand_point(): return (random.uniform(-1000, 1000), random.uniform(-1000, 1000))

        index_points = [rand_point() for _ in range(10000)]
        query_points = [rand_point() for _ in range(1000)]

        expected = []
        actual = []

        # Run the baseline slow tests to get the expected values.
        start = time.time()
        for query_point in query_points:
            expected.append(NearestNeighborIndex.find_nearest_slow(query_point, index_points))
        slow_time = time.time() - start

        # don't include the indexing time when benchmarking
        uut = NearestNeighborIndex(index_points)

        # Run the indexed tests
        start = time.time()
        for query_point in query_points:
            actual.append(uut.find_nearest(query_point))
        new_time = time.time() - start

        print(f"slow time: {slow_time:0.2f}sec")
        print(f"new time: {new_time:0.2f}sec")
        print(f"speedup: {(slow_time / new_time):0.2f}x")
