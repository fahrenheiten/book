# @typeassert(int,int)
# def add(x,y):
#     return x + y
# print(add(2,10))

from inspect import signature
from functools import wraps
def typeassert(*ty_args,**ty_kwargs):
    def decorate(func):
        # Если мы в оптимизированном режиме, отключаем проверку типов
        if not __debug__:
            return func
        # Отображаем имена аргументов функции на предоставленные типы
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args,**ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args,**kwargs):
            bound_types = sig.bind(*args,**kwargs)
            # Принудительно проверяем типы предоставленных аргументов ассертами
            for name,value in bound_types.arguments.items():
                if name in bound_types.arguments:
                    if not isinstance(value,bound_types.arguments[name]):
                        raise TypeError(
                            'Argument {} must be {}'.format(name,bound_types[name])
                            )
            return func(*args,**kwargs)
        return wrapper
    return decorate
@typeassert(int,z=int)
def spam(x,y,z=50):
    print(x,y,z)
    print(spam(1,3,5))
