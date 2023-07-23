nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Выводит кортеж как CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Сокращение (reduction) данных по полям в структуре данных
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print(min_shares)