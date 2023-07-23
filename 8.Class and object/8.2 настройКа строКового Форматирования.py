# _formats = {
# 'ymd' : '{d.year}-{d.month}-{d.day}',
# 'mdy' : '{d.month}/{d.day}/{d.year}',
# 'dmy' : '{d.day}/{d.month}/{d.year}'
# }
# class Date:
#     def __init__(self,year, month, day):
#         self.year = year
#         self.month = month
#         self.day = day
#
#     def __format__(self, code):
#         if code == '':
#             code = 'ymd'
#         fmt = _formats[code]
#         return fmt.format(d=self)
# d = Date(2022,5,29)
# print(format(d))
# print(format(d,'mdy'))
# print(format(d,'dmy'))

from datetime import date
d = date(2023,5,29)
today=format(d,'%A,%B %d,%Y')
print(today)



