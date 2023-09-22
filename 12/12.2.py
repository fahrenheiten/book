# from threading import Thread, Event
# import time
# # Код для выполнения в независимом потоке
# def countdown(n, started_evt):
#     print('countdown starting')
#     started_evt.set()
#     while n > 0:
#         print('T-minus',n)
#         n -= 1
#         time.sleep(2)
# # Создать объект события, который будет использован для сигнала о запуске
# started_evt = Event()
# # Запустить поток и передать событие запуска
# print('Launching coutdown')
# t = Thread(target=countdown,args=(10,started_evt))
# t.start()
# # Ждать запуска потока
# started_evt.wait()
# print('countdown is running')

# def longletters(s:str)->int:
# #обрезать конечные пробелы
#     p = len(s) - 1
#     while p >=0 and s[p] == ' ':
#         p -=1
#     # считаем количество букв в последнем слове
#     length = 0
#     while p>=0 and s[p] != ' ':
#         p -= 1
#         length += 1
#     return length
# print(longletters('Hello       word'))

import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()
    def start(self):
        t = threading.Thread(target=self.run)
        t.deamon = True
        t.start()
    def run(self):
        '''Запустить таймер и уведомлять ждущие потоки
        после каждого интервала'''
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()
    def wait_for_tick(self):
        '''Ждать следующего срабатывания таймера'''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()
    # Пример использования таймера
ptimer = PeriodicTimer(5)
ptimer.start()
# Два потока, синхронизирующихся по таймеру
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('T-minus', nticks)
        nticks -= 1
def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('Counting', n)
        n +=1
threading.Thread(target=countdown,args=(10,)).start()
threading.Thread(target=countdown,args=(5,)).start()