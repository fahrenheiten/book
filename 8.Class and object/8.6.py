# class Person:
#     def __init__(self,first_name):
#         self.first_name = first_name
#
#     # Функция-геттер
#     @property
#     def first_name(self):
#         return self._first_name
#
#     # Функция-сеттер
#     @first_name.setter
#     def first_name(self, value):
#         if not isinstance(value, str):
#             raise TypeError('Expected a string')
#
#         self._first_name = value
#
#     # Функция-делитер (необязательная)
#     @first_name.deleter
#     def first_name(self):
#         raise AttributeError("Can't delete attribute")
#
# a = Person('Guido')
# print(a.first_name)

import math
class Circle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def area(self):
        return math.pi * self.radius ** 2
    @property
    def perimiter(self):
        return 2 * math.pi * self.radius
c = Circle(4.0)
print(c.radius)
print(c.area)
print(c.perimiter)