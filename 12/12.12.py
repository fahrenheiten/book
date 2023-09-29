# def countdown(n):
#     while n > 0:
#         print('T-minus',n)
#         yield
#         n -= 1
#     print('Stop')
# # for _ in countdown(15):
# #     pass
# def countup(n):
#     x = 0
#     while x < 0:
#         print('Counting up',x)
#         yield
#         x +=1
#     print('Stop')
#
# from collections import deque
# class TaskScheduler:
#     def __init__(self):
#         self._task_queue = deque()
#     def new_task(self,task):
#         '''Допускает новую запущенную задачу в планировщик'''
#         self._task_queue.append(task)
#     def run(self):
#         '''Работает, пока не останется задач'''
#         while self._task_queue:
#             task = self._task_queue.popleft()
#             try:
#             # Работает до следующей инструкции yield
#                 next(task)
#                 self._task_queue.append(task)
#             except StopIteration:
#                 #Генератор более не выполняется
#                 pass
# sched = TaskScheduler()
# sched.new_task(countdown(10))
# sched.new_task(countdown(10))
# sched.new_task(countdown(10))
# sched.run()
# print('=================')
# from collections import deque
# class ActorShelduler:
#     def __init__(self):
#         self._actors = { } # Отображение имен на акторы
#         self._msg_queue = deque() # Очередь сообщений
#     def new_actor(self,name,actor):
#         '''
#         Допускает новый запущенный актор в планировщик и дает ему имя
#         '''
#         self._msg_queue.append((actor,None))
#         self._actors[name] = actor
#     def send(self,name,msg):
#         '''
#         Посылает сообщение актору с соответствующим именем
#         '''
#         actor = self._actors.get(name)
#         if actor:
#             self._msg_queue.append((actor,msg))
#     def run(self):
#         '''
#         Работает до тех пор, пока в очереди есть сообщения
#         '''
#         while self._msg_queue:
#             actor, msg = self._msg_queue.popleft()
#             try:
#                 actor.send(msg)
#             except StopIteration:
#                 pass
# if __name__ == '__main__':
#     def printer():
#         while True:
#             msg = yield
#             print('Got:',msg)
#     def counter(sched):
#         while True:
#             #Получить текущий счет
#             n = yield
#             if n == 0:
#                 break
#             #Послать задаче-принтеру
#             sched.send('printer',n)
#             #Послать следующий счет задаче-счетчику (рекурсивно)
#             sched.send('counter',n-1)
#     sched = ActorShelduler()
#     # Создать первоначальные акторы
#     sched.new_actor('printer',printer())
#     sched.new_actor('countrer',counter(sched))
#     # Послать начальное сообщение в счетчик для инициализации
#     sched.send('counter',100000)
#     sched.run()
print('=================')
from collections import deque
from select import select
# Эток класс представляет общее yield-событие в планировщике
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    def handle_resume(self, sched, task):
        pass
# Планировщик задач
class Scheduler:
    def __init__(self):
        self._numtasks = 0 # Общее количество задач
        self._ready = deque() # Задачи, готовые к запуску
        self._read_waiting = {} # Задачи, ждущие чтения
        self._write_waiting = {} # Задачи, ждущие записи
# Опрашивает на события ввода-вывода и перезапускает ждущие задачи
    def _iopolling(self):
        rset,wset,eset = select (self._read_waiting,
                                 self._write_waiting,[])
        for r in rset:
            evt,task = self._read_waiting.pop(r)
            evt.handle_resume = (self,task)
        for w in wset:
            evt, task = self._read_waiting.pop(w)
            evt.handle_resume = (self, task)

    def new(self, task):
        '''
        Добавляет новую запущенную задачу в планировщик
        '''

        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        '''
        Добавляет уже запущенную задачу в очередь готовых.
        msg – это то, что посылается в задачу, когда она
        возобновляется.
        '''

        self._ready.append((task, msg))

    # Добавляет задачу во множество чтения
    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)

    # Добавляет задачу во множество записи
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt,task)
    def run(self):
        '''
        апускает планировщик задач, пока задач не останется
        '''
        while self._numtasks:
            if not self._ready:
                self._iopolling()
            task,msg = self._ready.popleft()
            try:
                # Запустить корутину к следующему yield
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1
# Пример реализации сокетного ввода-вывода на основе корутин
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)
class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)
class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)
# Обертка вокруг объекта сокета для использования с yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock

    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)

    def send(self, data):
        return WriteSocket(self._sock, data)

    def accept(self):
        return AcceptSocket(self._sock)

    def __getattr__(self, name):
        return getattr(self._sock, name)
if __name__ == '__main__':
    from socket import socket,AF_INET,SOCK_STREAM
    import time


    # Пример функции, использующей генераторы. Это нужно вызывать
    # с использованием line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
            return b''.join(chars)
# Эхо-сервер, использующий генераторы
class EchoServer:
    def __init__(self,addr,sched):
        self.sched = sched
        self.sched.new(self.server_loop(addr))
    def server_loop(self,addr):
        s = Socket(socket(AF_INET,SOCK_STREAM))
        s.bind(addr)
        s.listen(5)
        while True:
            c,a = yield s.accept()
            print('Got connection from ', a)
            self.sched.new(self.client_handler(Socket(c)))
    def client_handler(self,client):
        while True:
            line = yield from readline(client)
            if not line:
                break
            line = b'GOT:' + line
            while line:
                nsent = yield client.send(line)
                line = line[nsent:]
                client.close()
            print('Client closed')
sched = Scheduler()
EchoServer(('',1600),sched)
sched.run()