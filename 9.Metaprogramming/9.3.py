# @somedecorator
# def add(x,y):
#     return x + y
# orig_add = add.__wrapped__
# orig_add(10,15)

def decorator1(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Decorator 1')
        return func(*args,**kwargs)
    return wrapper
def decorator2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Decorator 2')
        return func(*args,**kwargs)
    return wrapper
@decorator1
@decorator2
def add(x,y):
    return x+y
print(add(2,10))