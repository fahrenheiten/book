# text = 'yeah, but no, but yeah, but no, but yeah'
# text2 = text.replace('yeah','xxxxx')
# print(text2)
import re

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
# import re
# text3 = re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text)
# print(text3)

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text4 = datepat.sub(r'\3-\1-\2',text)
print(text4)
