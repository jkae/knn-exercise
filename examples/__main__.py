from .simple_example import *

tree = example_generate_tree()
print(tree)
print('\n')

[nn, dist] = example_find_nearest_neighbor()
print(nn) # 41.140259, -104.820236
