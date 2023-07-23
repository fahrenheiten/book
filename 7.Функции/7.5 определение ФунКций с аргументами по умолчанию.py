# _no_value = object()
#
# def spam(a, b=_no_value):
#     if b is _no_value:
#         print('No b value supplied')
#     return b
# print(spam(1))
# print(spam(1,2))
# print(spam(1,None))

x = 42
def spam(a, b=x):
    print(a,b)
print(spam(3))
x = 23
print(spam(4))