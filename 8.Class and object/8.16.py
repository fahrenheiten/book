import time
class Date:
# Основной конструктор
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon, t.tm_mday)
a = Date(2012, 12, 21) # Первичный
print(a)
b = Date.today() # Альтернативный
print(b)
