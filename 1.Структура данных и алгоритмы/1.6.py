from collections import defaultdict
d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
d['b'].add(5)
print(d)

d = {}
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('a',[]).append(3)
print(d)

# pairs = ['a':[4,6], 'b': [34], 'c': [4]]
d = {}
for key,value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)