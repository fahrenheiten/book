import types
from functools import wraps
#
# class Profiled:
#     def __init__(self,func):
#         wraps(func)(self)
#         self.ncalls = 0
#     def __call__(self, *args, **kwargs):
#         self.ncalls +=1
#         return self.__wrapped__(*args,**kwargs)
#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         else:
#             return types.MethodType(self,instance)
# @Profiled
# def add(x,y):
#     return x+y
# class Spam:
#     @Profiled
#     def bar(self,x):
#         print(self,x)
# print(add(2,6))
# print(add(10,50))
# print(add.ncalls)
# s=Spam()
# print(s.bar)

def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args,**kwargs):
        nonlocal ncalls
        ncalls +=1
        return func(*args,**kwargs)
    wrapper.ncalls = lambda:ncalls
    return wrapper
@profiled
def add(x,y):
    return x + y
print(add(25,45))