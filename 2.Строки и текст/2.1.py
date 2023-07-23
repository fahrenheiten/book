line = 'asdf fjdk; afed, fjek,asdf,   foo'
import re
line1=re.split(r'[;,\s]\s*',line)
line2 = re.split(r'(;|,|\s)\s*',line)
values = line2[::2]
delimiters = line2[1::2] + ['']
print(line1)
print(line2)
print(values)
print(delimiters)