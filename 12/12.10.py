from queue import Queue
from threading import Thread,Event
# # # Страж, использующийся для отключения
class ActrotExit(Exception):
    pass
class Actor:
    def __init__(self):
        self._mailbox = Queue()
    def send(self,msg):
        '''Посылает сообщение в актор'''
        self._mailbox.put(msg)
    def recv(self):
        '''Получаем входящие сообщение'''
        msg = self._mailbox.get()
        if msg is ActrotExit:
            raise ActrotExit()
        return msg
    def close(self):
        '''Закрывает актор и отключает его'''
        self.send(ActrotExit)
    def start(self):
        '''Запускает конкурентное выполнение'''
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()
    def _bootstrap(self):
        try:
            self.run()
        except ActrotExit:
            pass
        finally:
            self._terminated.set()
    def join(self):
        self._terminated.wait()
    def run(self):
        '''Запускает метод, который реализует пользователь'''
        while True:
            msg = self.recv()
# # Пример ActorTask
# class PrintActor(Actor):
#     def run(self):
#         while True:
#             msg = self.recv()
#             print('HAHAHHAH', msg)
# #Пример использования
# p = PrintActor()
# p.start()
# p.send('Hello')
# p.send('World')
# p.close()
# p.join()
# print('=============')
# def print_actor():
#     while True:
#         try:
#             msg = yield
#             print('Получил:',msg)
#         except GeneratorExit:
#             print('Прекращение')
# p = print_actor()
# next(p)
# p.send('Hello')
# p.send('World')
# p.close()
# class TaggedActor(Actor):
#     def run(self):
#         while True:
#             tag,*payload = self.recv()
#             getattr(self,'do_'+tag)(*payload)
#             # Методы, соответствующие различным тегам сообщений
#         def do_A(self,x):
#             print('Running A',x)
#         def do_B(self,y):
#             print('Running B',x,y)
# a = TaggedActor()
# a.start()
# a.send(('A',1))
# a.send(('B',3,4))
from threading import Event
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None
    def set_result(self,value):
        self._result = value
        self._evt.set()
    def result(self):
        self._evt.wait()
        return self._result
class Worker(Actor):
    def submit(self,func,*args,**kwargs):
        r = Result()
        self.send((func,args,kwargs,r))
        return r
    def run(self):
        while True:
            func,args,kwargs,r = self.recv()
            r.set_result(func(*args,**kwargs))
# Пример использования
worker = Worker()
worker.start()
r = worker.submit(pow,5,2)
print(r.result())
