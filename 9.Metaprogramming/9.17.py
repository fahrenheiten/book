# class NoMixedCaseMeta(type):
#     def __new__(cls, clsname,bases,clsdict):
#         for name in clsdict:
#             if name.lower() !=name:
#                 raise TypeError('Bad attribute name: ' + name)
#         return super().__new__(cls,clsname,bases,clsdict)
# class Root(metaclass=NoMixedCaseMeta):
#     pass
# class A(Root):
#     def foo_bar(self):
#         pass
# class B(Root):
#     def footBar(self):
#         pass

from inspect import signature
import logging

class MathSignaturesMeta(type):
    def __init__(self,clsname,bases,clsdict):
        super().__init__(clsname,bases,clsdict)
        sup = super(self,self)
        for name,value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            prev_dfn = getattr(sup,name,None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in %s. %s != %s',
                                    value.__qualname__,prev_sig,val_sig)
class Root(metaclass=MathSignaturesMeta):
    pass
class A(Root):
    def add(self,x,y):
        pass
    def spam(self,x,*,z):
        pass
class B(A):
    def add(self,a,b):
        pass
    def spam(self,x,z):
        pass


