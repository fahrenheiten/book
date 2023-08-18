def log_getattribute(cls):
    # Получение изначальной реализации
    orig_getattribute = cls.__getattribute__
    # Создание нового определения
    def new_getattribute(self,name):
        print('getting:',name)
        return orig_getattribute(self,name)
    # Прикрепление к классу и возврат
    cls.__getattribute__ = new_getattribute
    return cls
# Пример использования
@log_getattribute
class A:
    def __init__(self,x):
        self.x = x
    def spam(self):
        pass
a = A(42)
print(a.x)
print(a.spam())