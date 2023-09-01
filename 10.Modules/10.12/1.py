# from postimport import when_imported
# @when_imported('threading')
# def warn_thread(mod):
#     print('AAAAAAAAAA')
# import threading

from functools import wraps
from postimport import when_imported

def logged(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Calling', func.__name__,args,kwargs)
        return func(*args,**kwargs)
    return wrapper
@when_imported('math')
def add(mod):
    mod.cos = logged(mod.cos)
    mod.sin = logged(mod.sin)
