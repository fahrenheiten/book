# Вы хотите автоматически записывать порядок, в котором внутри тела класса
# определяются атрибуты и методы, что полезно при различных операциях (например, при сериалиации, отображении в базы данных и т. п.)

# from collections import OrderedDict
# #
# class Typed:
#     _expected_type = type(None)
#     def __init__(self,name = None):
#         self._name = name
#     def __set__(self,instance,value):
#         if not isinstance(value,self._expected_type):
#             raise TypeError('Expected' + str(self._expected_type))
#         instance.__dict__[self._name] = value
#
# class Iteger(Typed):
#     _expected_type = int
#
# class Float(Typed):
#     _expected_type = float
#
# class String(Typed):
#     _expected_type = str
#
# #
# class OrderedMeta(type):
#     def __new__(cls, clsname, bases,clsdict):
#         d = dict(clsdict)
#         order = []
#         for name,value in clsdict.items():
#             if isinstance(value,Typed):
#                 value._name = name
#                 order.append(name)
#         d['_order'] = order
#         return type.__new__(cls,clsname,bases,d)
#
#     @classmethod
#     def __prepare__(metacls, name, bases):
#         return OrderedDict()
# class Structure(metaclass=OrderedDict):
#     def as_cvs(self):
#         return ','.join(str(getattr(self,name)) for name in self._order)
# class Stock(Structure):
#     name = String()
#     shares = Iteger()
#     price = Float()
#     def __init__(self,name,shares,price):
#         self.name = name
#         self.shares = shares
#         self.price = price
# s = Stock('OOOO',100,490.1)
# s.name

from collections import OrderedDict

class NoDupOrderedDict(OrderedDict):
    def __init__(self,clsname):
        self.clsname = clsname
        super().__init__()
    def __setitem__(self, name,value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name,self.clsname))
        super().__setitem__(name,value)
class OrderedMeta(type):
    def __new__(cls, clsname,bases,clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] !='_']
        return type.__new__(cls,clsname,bases,d)
    @classmethod
    def __prepare__(cls,clsname,bases):
        return NoDupOrderedDict(clsname)
class A(metaclass=OrderedDict):
    def spam(self):
        pass
    def spam(self):
        pass
