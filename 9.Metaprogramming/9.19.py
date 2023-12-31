import operator

class StructTupleMeta(type):
    def __init__(cls,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls,name,property(operator.itemgetter(n)))
class StructTuple(tuple,metaclass=StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise TypeError('{}arguments requred'.format(len(cls._fields)))
        return super().__new__(cls,args)
class Stock(StructTuple):
    _fields = ['name','shares','price']
class Point(StructTuple):
    _fields = ['x','y']

s = Stock('Ivan',50,91.1)
print(s)
print(s[0])
print(s.name)
print(s.shares*s.price)