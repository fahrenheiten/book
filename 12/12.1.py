import time


def coutdown(n):
    while n > 0:
        print('T-minus',n)
        n -= 1
        time.sleep(3)
coutdown(3)
from threading import Thread
t = Thread(target=coutdown,args=(3,),daemon=True)
t.start()