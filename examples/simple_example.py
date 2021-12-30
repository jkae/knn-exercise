
# Please create a simple example use of the pynn library for your end user. Assume that the end
# user knows a lot about their subject matter but has only a basic understanding of Python.

# Meaningful examples may include reading a file, finding a few nearby points and writing them
# out to the console.

from pynn import kd_tree

def example_generate_tree():
    """
    Generate an example k-d tree from US capitals.
    """

    lat_lon = [
        (32.377716, -86.300568), # Montgomery
        (58.301598, -134.420212), # Juneau
        (33.448143, -112.096962), # Phoenix
        (34.746613, -92.288986), # Little Rock
        (38.576668, -121.493629), # Sacramento
        (39.739227, -104.984856), # Denver
        (41.764046, -72.682198), # Hartford
        (39.157307, -75.519722), # Dover
        (21.307442, -157.857376), # Honolulu
        (30.438118, -84.281296), # Tallahassee
        (33.749027, -84.388229), # Atlanta
        (43.617775, -116.199722), # Boise
        (39.798363, -89.654961), # Springfield
        (39.768623, -86.162643), # Indianapolis
        (41.591087, -93.603729), # Des Moines
        (39.048191, -95.677956), # Topeka
        (38.186722, -84.875374), # Frankfort
        (30.457069, -91.187393), # Baton Rouge
        (44.307167, -69.781693), # Augusta
        (38.978764, -76.490936), # Annapolis
        (42.358162, -71.063698), # Boston
        (42.733635, -84.555328), # Lansing
        (44.955097, -93.102211), # St. Paul
        (32.303848, -90.182106), # Jackson
        (38.579201, -92.172935), # Jefferson City
        (46.585709, -112.018417), # Helena
        (40.808075, -96.699654), # Lincoln
        (39.163914, -119.766121), # Carson City
        (43.206898, -71.537994), # Concord
        (40.220596, -74.769913), # Trenton
        (35.68224, -105.939728), # Santa Fe
        (35.78043, -78.639099), # Raleigh
        (46.82085, -100.783318), # Bismarck
        (42.652843, -73.757874), # Albany
        (39.961346, -82.999069), # Columbus
        (35.492207, -97.503342), # Oklahoma City
        (44.938461, -123.030403), # Salem
        (40.264378, -76.883598), # Harrisburg
        (41.830914, -71.414963), # Providence
        (34.000343, -81.033211), # Columbia
        (44.367031, -100.346405), # Pierre
        (36.16581, -86.784241), # Nashville
        (30.27467, -97.740349), # Austin
        (40.777477, -111.888237), # Salt Lake City
        (44.262436, -72.580536), # Montpelier
        (37.538857, -77.43364), # Richmond
        (47.035805, -122.905014), # Olympia
        (38.336246, -81.612328), # Charleston
        (43.074684, -89.384445), # Madison
        (41.140259, -104.820236) # Cheyenne
    ]

    root_node = kd_tree.kdTree(lat_lon)
    return root_node


def example_find_nearest_neighbor():
    """
    Find a k-d tree's nearest neighbor to a given point.

    Fort Collins, CO should be closer to Cheyenne, WY (41.140259, -104.820236) than Denver (39.739227, -104.984856)
    """

    tree = example_generate_tree()
    fort_collins = (40.5566532,-105.1026712) # 

    return kd_tree.kd_nearest_neighbor(tree, fort_collins)

