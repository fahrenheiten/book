# class Spam:
#     def __init__(self,name):
#         self.name = name
#         a = Spam('Ivan')
#         b = Spam('QQQQ')
#
# class NoInstances(type):
#     def __call__(self, *args, **kwargs):
#         raise TypeError('Cant instantiate directly')
#
# class Spam(metaclass=NoInstances):
#     @staticmethod
#     def grok(x):
#         print('Spam.grok')
# Spam.grok(52)
# s = Spam()

#  класс, из которого можно создать только один экземпляр

# class Singleton(type):
#     def __init__(self,*args,**kwargs):
#         self._instance = None
#         super().__init__(*args,**kwargs)
#     def __call__(self, *args, **kwargs):
#         if self._instance is None:
#             self._instance = super().__call__(*args,**kwargs)
#             return self._instance
#         else:
#             return self._instance
# class Spam(metaclass=Singleton):
#     def __init__(self):
#         print('Creating Spam')
# a = Spam()
# b = Spam()
# print(a is b )
# c = Spam()
# print(a is c)
#создавать кешированные экземпляры
# import weakref
# class Cached(type):
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self._cache = weakref.WeakValueDictionary()
#     def __call__(self,*args):
#         if args in self._cache:
#             return self._cache[args]
#         else:
#             obj = super().__call__(*args)
#             self._cache[args] = obj
#             return obj
# class Spam(metaclass=Cached):
#     def __init__(self,name):
#         print('Creating Spam({!r})'.format(name))
#         self.name = name
# a = Spam('Guido')
# b = Spam('Ivan')
# c = Spam('Ivan')
# print(a is b)
# print(a is c)
# print(b is c)

# метакласс, то
# вам может потребоваться спрятать классы за какой­то дополнительной фабричной функцией

class _Spam:
    def __init__(self):
        print('Creating Spam!')
    _spam_instance = None
    def Spam():
        global _spam_instance
        if _spam_instance is not None:
            return _spam_instance
        else:
            _spam_instance = _Spam()
            return _spam_instance
