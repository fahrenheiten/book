# with  open('somefile.txt','xt') as file:
#     file.write('Hello')
import os
if not os.path.exists('somefile.txt'):
    with open('somefile.txt','wt') as file:
        file.write('111111')
else:
    print('File already exists')