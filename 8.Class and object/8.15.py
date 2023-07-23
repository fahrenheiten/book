# class A:
#     def spam(self,x):
#         pass
#     def foo(self):
#         pass
# class B:
#     def __init__(self):
#         self._a = A()
#     def bar(self):
#         pass
# # Показывает все методы, определенные на классе A
# def __getattr__(self,name):
#     return getattr(self._a,name)
# b = B()
# print(b.bar())
# # print(b.spam(52))

class Proxy:
    def __init__(self,obj):
        self._obj = obj
# Делегирует поиск атрибутов внутреннему obj
    def __getattr__(self, item):
        print('getattr:',item)
        return getattr(self._obj,item)
# Делегирует присвоение атрибутов
    def __setattr__(self,name,value):
        if name.startswith('_'):
            super().__setattr__(name,value)
        else:
            print('setattr:',name,value)
            setattr(self._obj,name,value)
# Делегирует удаление атрибутов
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('delattr:',name)
            delattr(self._obj,name)
class Spam:
    def __init__(self,x):
        self.x = x
    def bar(self,y):
        print('Spam.bar:',self.x,y)
s = Spam(10)
p = Proxy(s)
print(p.x)
print(p.bar(15))
p.x = 555
print(p.x)
