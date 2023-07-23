from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for k in d:
    print(k,d[k])


import json
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
print(json.dumps(d))