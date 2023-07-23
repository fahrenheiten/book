# Срезание пробелов
s = ' hello world \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())
# Срезание символов
t = '-----hello====='
print(t.lstrip('-'))
print(t.strip('=-'))
print(s.replace(' ',''))