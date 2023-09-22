from collections import defaultdict
class Exchange:
    def __init__(self):
        self._subscribers = set()
    def attach(self,task):
        self._subscribers.add(task)
    def detach(self,task):
        self._subscribers.remove(task)
    def send(self,msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)
#Словарь всех созданных пунктов обмена
_exchanges = defaultdict(Exchange)
# Вернуть экземпляр Exchange, ассоциированный с переданным именем
def get_exchange(name):
    return _exchanges[name]
exchange = get_exchange('my_exchange')
class Task:
    def send(self,msg):
        print('Hello:',msg)
task_1 = Task()
task_2 = Task()
exchange.attach(task_1)
exchange.attach(task_2)
exchange.send('Hello urka')
exchange.detach(task_1)