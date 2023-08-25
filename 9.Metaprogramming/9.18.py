# Пример ручного создания класса из частей
# def __init__(self,name,shares,price):
#     self.name = name
#     self.shares = shares
#     self.price = price
# def cost(self):
#     return self.shares*self.price
# cls_dict={
#     '__init__':__init__,
#     'cost':cost,
#     '__bases__': (object,)
# }
# # Создание класса
# import types
#
# Stock = types.new_class('Stock',{},{},lambda ns: ns.update(cls_dict))
# Stock.__module__=__name__
#
# s = Stock('ACME',50,90.1)
# print(s.cost())

import operator
import types
import sys

def named_tuple(classname,fieldnames):
    # Наполняем словарь акцессоров свойств полей
    cls_dict = {name:property(operator.itemgetter(n))
                for n, name in enumerate(fieldnames)}

    # Создаем функцию __new__ и добавляем ее в словарь класса
    def __new__(cls,*args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))
        return tuple.__new__(cls,args)

    cls_dict['__new__'] = __new__
    # Создаем класс
    cls = types.new_class(classname,(tuple,),{},lambda ns: ns.update(cls_dict))
    # Устанавливаем модуль класса на модуль вызывающего
    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls
Point = named_tuple('Point',['x','y'])
print(Point)
p = Point(4,30,55)
print(len(p))
print(p.x)
print(p.y)
print(p.x == 10)
print('%s %s' % p)