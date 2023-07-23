# class LoggedMappingMixin:
#     '''Добавляем логирование для операций get/set/delete в целях отлатки'''
#     __slots__ = ()
#
#     def __getitem__(self,key):
#         print('Getting ' + str(key))
#         return super().__getitem__(key)
#     def __setitem__(self, key, value):
#         print('Setting {} = {!r}'.format(key,value))
#         return super().__setitem__(key,value)
#     def __delitem__(self, key):
#         print('Deleting ' + str(key))
#         return super().__delitem__(key)
# class SetOnceMappingMixin:
#     '''Позволяет уставливать ключ только один раз'''
#     __slots__ = ()
#     def __setitem__(self, key, value):
#         if key in self:
#             raise KeyError(str(key)+'already set')
#         return super().__setitem__(key,value)
#
# class StringKeysMappingMixin:
#     '''запрещает ключам быть чем-то кроме строк.'''
#     __slots__ = ()
#     def __setitem__(self, key, value):
#         if not isinstance(key,str):
#             raise TypeError('keys must be strings')
#         return super().__setitem__(key,value)
#
# class LoggedDict(LoggedMappingMixin,dict):
#     pass
# d = LoggedDict()
# d['x']=23
# d['x']
# del d['x']
# from collections import defaultdict
# class SetOnceDufaultDict(SetOnceMappingMixin,defaultdict):
#     pass
# d = SetOnceDufaultDict(list)
# d['x'].append(52)
# d['y'].append(54)
# d['x'].append(60)
# d['x'] = 23
# from collections import OrderedDict
# class StringOrderDict(StringKeysMappingMixin,
#                       SetOnceMappingMixin,
#                       OrderedDict):
#     pass
# d = StringOrderDict()
# d['x'] = 23
# d[42]=50
# d['x']=42
# print('====================')
#
# class RecstrictKeysMixin:
#     def __init__(self,*args,_restrict_key_type,**kwargs):
#         self.__resrtict_key_type = _restrict_key_type
#         super().__init__(*args,**kwargs)
#
#     def __setitem__(self, key, value):
#         if not isinstance(key,self.__resrtict_key_type):
#             raise TypeError('Keys must be' + str(self.__resrtict_key_type))
#         super().__setitem__(key,value)
# class RDict(RecstrictKeysMixin,dict):
#     pass
# d = RDict(_restrict_key_type=str)
# e = RDict([('name','Ivan'),('n',30)],_restrict_key_type=str)
# f = RDict(name = 'Ivan',n = 30,_restrict_key_type=str)
# print(f)
# f[42] = 65

print('==========')

def LoggeedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self,key):
        print('Getting' + str(key))
        return cls_getitem(self,key)
    def __setitem__(self,key,value):
        print('Setting {} = {!r}'.format(key,value))
        return cls_setitem(self,key,value)
    def __delitem__(self,key):
        print('Deliting '+ str(key))
        return cls_delitem(self,key)
    cls.__getitem__ = __getitem__
    cls.__setitem__= __setitem__
    cls.__delitem__ = __delitem__
@LoggeedMapping
class LoggedDict(dict):
    pass
d = LoggedDict()
d['x']=52
