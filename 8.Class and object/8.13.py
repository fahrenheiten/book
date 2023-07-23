# # # Базовый класс. Использует дескриптор для установки значения
# class Description:
#     def __init__(self, name=None, **opts):
#         self.name = name
#         for k, v in opts.items():
#             setattr(self, k, v)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# # Дескриптор для принудительного определения типов
# class Typed(Description):
#     expected_type = type(None)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.expected_type):
#             raise TypeError('expected' + str(self.expected_type))
#         super().__set__(instance, value)
#
#
# # Дескриптор для принудительного определения значений
# class Usingned(Description):
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Expected >=0')
#         super().__set__(instance, value)
#
#
# class MaxSized(Description):
#     def __init__(self, name=None, **opts):
#         if 'size' not in opts:
#             raise TypeError('missing size option')
#         super().__init__(name, **opts)
#
#     def __set__(self, instance, value):
#         if len(value) >= self.size:
#             raise TypeError('size must be < ' + str(self.size))
#         super().__set__(instance, value)
#
#
# class Integer(Typed):
#     expected_type = int
#
#
# class UsingnedInteged(Integer, Usingned):
#     pass
#
#
# class Float(Typed):
#     expected_type = float
#
#
# class UsingnedFloat(Float, Usingned):
#     pass
#
#
# class String(Typed):
#     expected_type = str
#
#
# class SizeString(String, MaxSized):
#     pass
#
#
# class Stock:
#     # Определяем ограничения
#     name = SizeString('name', size=10)
#     shares = UsingnedInteged('shares')
#     price = UsingnedFloat('price')
#
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
#
#
# s = Stock('ACME', 50, 91.1)
# print(s.name)
# print(s.shares)
#
# # Декоратор класса для применения ограничений
# def check_attributes(**kwards):
#     def decorates(cls):
#         for k,v in kwards.items():
#             if isinstance(v,Description):
#                 v.name = k
#                 setattr(cls,k,v)
#             else:
#                 setattr(cls,k,v(k))
#         return cls
#     return decorates
# @check_attributes(name = SizeString(size = 8),
#                   shares = UsingnedInteged,
#                   price = UsingnedFloat)
# class Stock:
#     def __init__(self, name, shares, price):
#         self.name = name
#         self.shares = shares
#         self.price = price
# s = Stock('ACME', 50, 91.1)
# print(s.name)
# print(s.shares)

print('================')


# Базовый класс. Использует дескриптор для установки значения
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


# Декоратор для применения проверки типов
def Typed(expected_type, cls=None):
    if cls is None:
        return lambda cls: Typed(expected_type, cls)
    super_set = cls.__set__

    def __set__(self, instance, value):
        if not isinstance(value, expected_type):
            raise TypeError('expected ' + str(expected_type))

        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Декоратор для беззнаковых значений
def Unsigned(cls):
    super_set = cls.__set__

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Декоратор, разрешающий значения с определенным размером
def MaxSized(cls):
    super_init = cls.__init__

    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super_init(self, name, **opts)

    cls.__init__ = __init__

    super_set = cls.__set__

    def __set__(self, instance, value):
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size))
        super_set(self, instance, value)

    cls.__set__ = __set__
    return cls


# Специализированные дескрипторы
@Typed(int)
class Integer(Descriptor):
    pass


@Unsigned
class UnsignedInteger(Integer):
    pass


@Typed(float)
class Float(Descriptor):
    pass


@Unsigned
class UsingnedFloat(Float):
    pass


@Typed(str)
class String(Descriptor):
    pass


@MaxSized
class SizedString(String):
    pass

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
s = Stock('ACME', 50., 91.1)
print(s.name)
print(s.shares)
