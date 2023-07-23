from fnmatch import fnmatch,fnmatchcase
print(fnmatch('foo.txt','*.txt'))
print(fnmatch('foo.txt','?oo.txt'))
addresses = [
'5412 N CLARK ST',
'1060 W ADDISON ST',
'1039 W GRANVILLE AVE',
'2122 N CLARK ST',
'4802 N BROADWAY',
]
print([addr for addr in addresses if fnmatchcase(addr,'*ST')])