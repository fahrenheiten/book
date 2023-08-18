# from functools import wraps
# def optinal_debug(func):
#     @wraps(func)
#     def wrapper(*args,debug = False,**kwargs):
#         if debug:
#             print('Calling', func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
# @optinal_debug
# def spam(a,b,c,d,e,f):
#     print(a,b,c,d,e,f)
# spam(1,2,3,4,5,6)
# spam(1,2,3,4,5,6,debug=True)

from functools import wraps
import inspect

def optinal_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError('debug argument already defined')
    @wraps(func)
    def wrapper(*args,**kwargs):
        if debug:
            print('Calling',func.__name__)
        return func(*args,**kwargs)

    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug',
                                   inspect.Parameter.KEYWORD_ONLY,
                                   default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
@optinal_debug
def add(x,y):
    return x+y
print(inspect.signature(add))
(x, y, *, debug=False)
add(2,3)