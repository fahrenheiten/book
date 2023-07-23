a = {
'x' : 1,
'y' : 2,
'z' : 3
}
b = {
'w' : 10,
'x' : 11,
'y' : 2
}

# Находим общие ключи
print(a.keys() & b.keys())
# Находим ключи, которые есть в a, но которых нет в b
print(a.keys() - b.keys())
# Находим общие пары (key,value)
print(a.items() & b.items())
# Создаем новый словарь, из которого удалены некоторые ключи
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)