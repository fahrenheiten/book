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
from collections import deque
class ActorShelduler:
    def __init__(self):
        self._actors = { } # Отображение имен на акторы
        self._msg_queue = deque() # Очередь сообщений
    def new_actor(self,name,actor):
        '''
        Допускает новый запущенный актор в планировщик и дает ему имя
        '''
        self._msg_queue.append((actor,None))
        self._actors[name] = actor
    def send(self,name,msg):
        '''
        Посылает сообщение актору с соответствующим именем
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor,msg))
    def run(self):
        '''
        Работает до тех пор, пока в очереди есть сообщения
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            try:
                actor.send(msg)
            except StopIteration:
                pass
if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('Got:',msg)
    def counter(sched):
        while True:
            #Получить текущий счет
            n = yield
            if n == 0:
                break
            #Послать задаче-принтеру
            sched.send('printer',n)
            #Послать следующий счет задаче-счетчику (рекурсивно)
            sched.send('counter',n-1)
    sched = ActorShelduler()
    # Создать первоначальные акторы
    sched.new_actor('printer',printer())
    sched.new_actor('countrer',counter(sched))
    # Послать начальное сообщение в счетчик для инициализации
    sched.send('counter',100000)
    sched.run()


