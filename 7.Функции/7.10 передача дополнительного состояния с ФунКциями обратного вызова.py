def apply_async(func, args, *, callback):
# Вычислить результат
    result = func(*args)
# Вызвать функцию обратного вызова с результатом
    callback(result)
def print_result(result):
    print('Got:',result)
def add(x,y):
    return x + y
print(apply_async(add,(10,50),callback=print_result))

def make_handler():
    sequence = 0
    def handler(result):
        nonlocal sequence
        sequence +=1
        print('[{}] Got : {}'.format(sequence,result))
    return handler
handler = make_handler()
next(handler)
apply_async(add, (2, 3), callback=handler.send)

class SequenceNo:
    def __init__(self):
        self.sequence = 0

    def handler(result, seq):
        seq.sequence += 1
        print('[{}] Got: {}'.format(seq.sequence, result))
seq = SequenceNo()
from functools import partial
print(apply_async(add, (2, 3), callback=partial(handler, seq=seq)))
