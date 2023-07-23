# def sample():
#     n = 0
#     # Функция-замыкание
#     def func():
#         print('n=', n)
#
#     def get_n():
#         return n
#     def set_n(value):
#         nonlocal n
#         n = value
#
#     # Прикрепление в качестве атрибутов функции
#     func.get_n = get_n
#     func.set_n = set_n
#     return func
# f = sample()
# f()
# f.set_n(10)
# f()
# f.get_n(20)

import sys
class ClosureInstance:
    def __init__(self,local = None):
        if local is None:
            locals = sys._getframe(1).f_locals
# Обновить словарь экземпляра вызываемыми объектами
        self.__dict__.update((key,value) for key, value in locals.items()
                             if callable(value))
# перегружаем специальные методы
    def __len__(self):
        return self.__dict__['__len__']()
def Stack():
    items = []
    def push(item):
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()
s = Stack()
print(s)
s.push(10)
s.push(20)
s.push('XXXX')
print(len(s))
print(s.pop())
print(s.pop())
print(s.pop())

print('============')


