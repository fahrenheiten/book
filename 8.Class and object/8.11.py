import math


# class Structure:
# # Переменная класса, которая определяет ожидаемые поля
#     _fields = []
#     def __init__(self,*args):
#         if len(args) != len(self._fields):
#             raise TypeError('Expected {} arguments'.format(len(self._fields)))
#         # Устанавливает аргументы
#         for name,value in zip(self._fields,args):
#             setattr(self,name,value)
# if __name__ == '__main__':
#     class Stock(Structure):
#         _fields = ['name','shares','price']
#     class Point(Structure):
#         _fields = ['x','y']
#     class Circle(Structure):
#         _fields = ['radius']
#         def area(self):
#             return math.pi * self.radius **2
# s = Stock('ACME',50,91.5)
# a = Circle(4.5)
# print(a.area)

class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self.fields)))
        # Установка всех позиционных аргументов
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

    # Установка оставшихся именованных аргументов
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))
    # Проверка на оставшиеся любые другие аргументы
        if kwargs:
            raise TypeError('Invalid argument(s): {}'.format(','.join(kwargs)))


if __name__ == '__main__':
    class Stock(Structure):
        _fields = ['name', 'shares', 'price']

    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, price=91.1)
    s3 = Stock('ACME', shares=50, price=91.1)
    print(s1.__dict__)
    print(s2.__dict__)
    print(s3.__dict__)
