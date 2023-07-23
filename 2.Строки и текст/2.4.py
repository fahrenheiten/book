text = 'yeah, but no, but yeah, but no, but yeah'
# Точное совпадение
print(text == 'yeah')
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
import re
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('now')

datepat = re.compile(r'\d+/\d+/\d+')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))
m = datepat.match('11/27/2012')
print(m.group(0))

