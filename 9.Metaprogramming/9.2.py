import time
from functools import wraps

def timethis(func):
    '''Декоратор, который показывает время выполнениия'''
    @wraps(func)
    def wraper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wraper
@timethis
def coutdown(n:int):
    while n > 0:
        n -=1
coutdown(100000)
print(coutdown.__name__)
print(coutdown.__doc__)
print(coutdown.__annotations__)