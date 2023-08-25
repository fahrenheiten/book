class MyMeta(type):
# Необязательно
@classmethod
def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
# Кастомная обработка

    return super().__prepare__(name, bases)
# Требуется
def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
# Кастомная обработка

    return super().__new__(cls, name, bases, ns)
# Требуется
def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
# Кастомная обработка

    super().__init__(name, bases, ns)