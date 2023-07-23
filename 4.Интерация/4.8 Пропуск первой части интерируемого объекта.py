from itertools import islice
items = ['a','b','c',1,4,20,30]
for x in islice(items,3,None):
    print(x)