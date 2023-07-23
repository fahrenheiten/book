# # Дескриптор атрибута для целочисленного атрибута с проверкой типа
# class Integeer:
#     def __init__(self,name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value,int):
#             raise TypeError('Expected an int')
#         instance.__dict__[self.name] = value
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
# class Point:
#     x = Integeer('x')
#     y = Integeer('y')
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
# p = Point(10,15)
# print(p.x)
# print(p.y)
# print(p.x)

# Дескриптор для атрибута с проверкой типа
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
def __set__(self, instance, value):
    if not isinstance(value, self.expected_type):
        raise TypeError('Expected ' + str(self.expected_type))
    instance.__dict__[self.name] = value
def __delete__(self, instance):
    del instance.__dict__[self.name]
# Декоратор класса, который применяет его к выбранным атрибутам
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
        # Attach a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return decorate
@typeassert(name=str,shares=int,price=float)
class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
a = Stock('Ivan',5,5.1)
print(a.name)
print(a.shares)
print(a.price)
