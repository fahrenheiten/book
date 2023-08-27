def coutdown(n):
    while n >0:
        print('T-minus',n)
        n -= 1
    print('Blastoff!')
import dis
dis.dis(coutdown)