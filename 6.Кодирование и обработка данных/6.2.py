import json

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}
# json_str = json.dumps(data)
# print(json_str)
# Запись JSON-данных
with open('data.json','w') as file:
    json.dump(data,file)
# Чтение данных
with open('data.json','r') as file:
    data = json.load(file)
    print(data)
print('-----------------')

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
from collections import OrderedDict
data = json.loads(s,object_pairs_hook=OrderedDict)
print(data)
#Вот как вы можете превратить словарь JSON в объект Python
class JSONObject:
    def __init__(self,d):
        self.__dict__=d
data = json.loads(s,object_hook=JSONObject)
print(data.name)
print(data.shares)
print(data.price)
# print(json.dumps(data,indent=4))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

def serilaze(obj):
    d = {'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d


# Словарь отображения имен на известные классы
classes = {
'Point' : Point
}
def unserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Создание экземпляра без вызова __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
        else:
            return d
p = Point(2,3)
s = json.dumps(p,default=serilaze)
print(s)