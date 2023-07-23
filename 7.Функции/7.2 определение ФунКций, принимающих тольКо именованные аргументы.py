def recv(max,*,block):
    'Reveices a messages'
    pass
# print(recv(1024,True))
print(recv(1024,block=True))
# функциях, которые принимают различное количество позиционных аргументов
def minimum(*values,clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m
print(minimum(1,2,3,-5,10,-10))