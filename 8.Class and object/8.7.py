# class A:
#     def spam(self):
#      print('A.spam')
# class B(A):
#     def spam(self):
#         print('B.spam')
#         super().spam()

# class Proxy:
#     def __init__(self,obj):
#         self._obj = obj
#     #Передача поиска по атрибута внутреннему obj
#     def __getattr__(self, item):
#         return getattr(self._obj,item)
#     # Передача присвоения атрибута
#     def __setattr__(self, item, value):
#         if item.startswith('_'):
#             super().__setattr__(item,value)
#         else:
#             setattr(self._obj,item,value)
# c = Proxy('sdfd')
# print(c.__getattr__('sdfd'))


# class Base:
#     def __init__(self):
#         print('Base.__init__')
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         # Base.__init__(self)
#         print('A.__init__')
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         # Base.__init__(self)
#         print('B.__init__')
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         # A.__init__(self)
#         # B.__init__(self)
#         print('C.__init__')
# c = C()
# print(C.__mro__)

# class A:
#     def spam(self):
#         print('A.spam')
#         super().spam()
# class B:
#     def spam(self):
#         print('B.spam')
# class C(A,B):
#     pass
# c = C()
# print(c.spam())