###### 0123456789012345678901234567890123456789012345678901234567890'
# record = '....................100 .......513.25 ..........'
# cost = int(record[20:32] * float(record[40:48]))
# # print(cost)
# shares = slice(20,32)
# price = slice(40,48)
# cost = int(record[shares] * float(record[shares]))

# items = [0,1,2,3,4,5,6,7,8,9]
# a = slice(2,6)
# print(items[2:4])
# print(items[a])
# items[a] = [10,11]
# print(items)
# del items[a]
# print(items)

s = 'Helloword'
a = slice(5,10,2)
for i in range(*a.indices(len(s))):
    print(s[i])
