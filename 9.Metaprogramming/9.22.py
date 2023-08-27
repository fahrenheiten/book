import time
from contextlib import contextmanager
@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}:{}'.format(label,end-start))
#Exsample
with timethis('coutinng'):
    n = 1000000
    while n > 0:
        n -=1
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
items = [1,2,4]
with list_transaction(items) as working:
    working.append(4)
    working.append(6)
print(items)
with list_transaction(items) as working:
    working.append(10)
    working.append(15)
    raise RuntimeError('oops')
print(items)
