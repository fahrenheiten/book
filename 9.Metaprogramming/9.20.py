# class Spam:
#     def bar(self,x:int,y:int):
#         print('Bar 1:',x,y)
#
#     def bar(self,s:str,n:int = 0):
#         print('Bar 2:',s,n)
# s = Spam()
# print(s.bar(2,5))
# print(s.bar('hello'))

# import inspect
# import types
#
# class MultiMethod:
#     '''Представляет один мультиметод.'''
#     def __init__(self,name):
#         self._methods = {}
#         self.__name__ = name
#     def register(self,meth):
#         '''Регистрирует новый метод как мультиметод'''
#         sig = inspect.signature(meth)
#         # Создание сигнатуры типа из аннотаций методов
#         types = []
#         for name,parm in sig.parameters.items():
#             if name == 'self':
#                 continue
#             if parm.annotation is inspect.Parameter.empty:
#                 raise TypeError(
#                     'Argument {} must be annotated with a type'.format(name)
#                 )
#             if not isinstance(parm.annotation, type):
#                 raise TypeError(
#                     'Argument {} must be annotated with a type'.format(name)
#                 )
#             if parm.default is not inspect.Parameter.empty:
#                 self._methods[tuple(types)] = meth
#             types.append(parm.annotation)
#         self._methods[tuple(types)] = meth
#     def __call__(self, *args):
#         '''Вызов метода базируется на сигнатуре типа аргументов'''
#         types = tuple(type(arg) for arg in args[1:])
#         meth = self._methods.get(types,None)
#         if meth:
#             return meth(*args)
#         else:
#             raise TypeError('No matching method for types {}'.format(types))
#     def __get__(self, instance, cls):
#         '''Метод дескриптора, необходимый для работы вызовов в классе'''
#         if instance is not None:
#             return types.MethodType(self,instance)
#         else:
#             return self
# class MultiDict(dict):
#     '''Специальный словарь для создания мультиметодов в метаклассе'''
#     def __setitem__(self, key, value):
#         if key in self:
#             #Если ключ уже существует, он должен быть мультиметодом
#             #или вызываемым объектом
#             current_value = self[key]
#             if isinstance(current_value, MultiMethod):
#                 current_value.register(value)
#             else:
#                 mvalue = MultiMethod(key)
#                 mvalue.register(current_value)
#                 mvalue.register(value)
#                 super().__setitem__(key,value)
#         else:
#             super().__setitem__(key,value)
# class MultipleMeta(type):
#     '''Метакласс, который позволяет множественную диспетчеризацию методов'''
#     def __new__(cls, clsname,bases,clsdict):
#         return type.__new__(cls,clsname,bases,dict(clsdict))
#     @classmethod
#     def __prepare__(cls, clsname, bases):
#         return MultiDict()
#     #Чтобы использовать этот класс
# class Spam(metaclass=MultipleMeta):
#     def bar(self,x:int,y:int):
#         print('Bar 1:',x,y)
#     def bar(self,s:str,n:int = 0):
#         print('Bar 2:',s,n)
# # Пример: перегруженный __init__
# import time
# class Date(metaclass=MultipleMeta):
#     def __init__(self,year: int, month:int,day:int):
#         self.year = year
#         self.month = month
#         self.day = day
#     def __init__(self):
#         t = time.localtime()
#         self.__init__(t.tm_year,t.tm_mon,t.tm_mday)
# s = Spam()
# print(s.bar(2,3))
# print(s.bar('hello'))
# print(s.bar('hello',5))
# print(s.bar (10,'hello'))
# print(s.bar(2,'hello'))
# print(s.bar(2,'hello'))
# Перегруженный __init__
# d = Date(2012,12,21)
# # Получить сегодняшнюю дату
# # print(d.year)
# # print(d.month)
# # print(d.day)

import types
class multimethod:
    def __init__(self,func):
        self._method = {}
        self.__name__ = func.__name__
        self._default = func

    def match(self,*types):
        def register(func):
            ndefults = len(func.__defaults__) if func.__defaults__ else 0
            for n in range(ndefults+1):
                self._method[types[:len(types)-n]] = func
            return self
        return register
    def __call__(self, *args):
        types = tuple (type(args) for arg in args[:1])
        meth = self._method.get(types,None)
        if meth:
            return meth(*args)
        else:
            return self._default(*args)

    def __get__(self, instance, cls):
        if instance is not None:
            return types.MethodType(self,instance)
        else:
            return self
class Spam:
    @multimethod
    def bar(self,*args):
        # Если нет совпадений, вызывается дефолтный метод
        raise TypeError('No matching method for bar')
    @bar.match(int,int)
    def bar(self,x,y):
        print('Bar 1:',x,y)
    @bar.match(str,int)
    def bar(self,s,n=0):
        print('Bar 2 :',s,n)

s = Spam
# print(s.bar(10,2))
print(s.bar('hello'))
