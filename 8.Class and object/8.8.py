# class Person:
#     def __init__(self,name):
#         self.name = name
#
#     # Функция-геттер
#     @property
#     def name(self):
#         return self._name
#
#     # Функция-сеттер
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError('Expected a string')
#         self._name = value
#
#     # Функция-делитер
#     @name.deleter
#     def name(self):
#         raise AttributeError("Can't delete attribute")
#
# class Subperson(Person):
#     @property
#     def name(self):
#         print('Getting name')
#         return super().name
#
#     @name.setter
#     def name(self,value):
#         print('Setting name to',value)
#         super(Subperson,Subperson).name.__set__(self,value)
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         super(Subperson,Subperson).name.__delete__(self)
# a = Subperson('Guido')
# print(a.name)
# a.name = 'Ivan'
# print(a.name)

# Дескриптор
class String:
    def __init__(self,name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if not instance(value, str):
            raise TypeError('Expected a string')
        instance.__dict__[self.name] = value
# Класс с дескриптором
class Person:
    name = String('name')
    def __init__(self,name):
        self.name = name
# Расширение дескриптора свойством
class SubPerson(Person):
    @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self,value):
        print('Setting name to ', value)
        super(SubPerson,SubPerson).name.__set__(self,value)

    @name.deleter
    def name(self):
        print('Delete name')
        super(SubPerson,SubPerson).name.__delete__(self)

a = SubPerson('Guido')
print(a.name)