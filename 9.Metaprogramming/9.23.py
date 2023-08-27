# a = 25
# exec('b = a + 30')
# print(b)
def test():
    a = 30
    loc = locals()
    exec('b = a + 30')
    print(loc['b'])
test()
print('===========')
def test_2():
    x = 0
    loc = locals()
    print('before: ',loc)
    exec('x +=1')
    print('after: ',loc)
    print('x =',x)


test_2()
print('==========')
def test_3():
    x = 0
    loc = locals()
    print(loc)
    exec('x +=1')
    print(loc)
    locals()
    print(loc)
test_3()
print('==========')
def test_4():
    a = 20
    loc = {'a':a}
    glb = { }
    exec('b = a +1',glb,loc)
    b = loc['b']
    print(b)
test_4()
