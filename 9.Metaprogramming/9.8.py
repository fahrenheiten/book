from functools import wraps


class A:
# Декоратор как метод экземпляра
    def decorator1(self,func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            print('Decorator 1')
            return func(*args,**kwargs)
        return wrapper
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)
        return wrapper
# Как метод экземпляра
a = A()
@a.decorator1
def spam():
    pass
# Как метод класса
@A.decorator2
def grok():
    pass

class Person:
    # Создание экземпляра свойства
    firs_name = property()
    # Применение методов декоратора
    @firs_name.getter
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,value):
        if not isinstance(value,str):
            raise TypeError('Expected a string')
        self._first_name = value



