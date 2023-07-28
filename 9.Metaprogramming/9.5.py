from functools import wraps,partial
import logging
#
def attach_wrapper(obj, func = None):
    if func is None:
        return partial(attach_wrapper,obj)
    setattr(obj,func.__name__,func)
    return func
def logger(level,name = None,message=None):
    '''
    :param level:уровень логирования 
    :param name: название логера
    :param message: сообщение в лог
    Если name, massage не определены, они будут дефолтными от имени функции и ее модуля
    '''
    def decorete(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args,**kwargs):
            log.log(level,logsmg)
            return func(*args,**kwargs)
        #
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
        @attach_wrapper(wrapper)
        def set_massage(newmsg):
            nonlocal logmsg
            logmsg = newmsg
    return decorete
    @logged(logging.DEBUG)
    def add(x,y):
        return x+y
    @logged(logging.CRITICAL,'example')
    def spam():
        print('Spam!')
    logging.basicConfig(level=logging.DEBUG)
    add(2,3)
