items = ['a', 'b', 'c']
from itertools import permutations,combinations
# for p in permutations(items):
#     print(p)
# items = ['a', 'b', 'c']
# from itertools import permutations
# for p in permutations(items,2):
#     print(p)
for c in combinations(items,1):
    print(c)
for x in combinations_with_replacement(items,3):
    print(x)