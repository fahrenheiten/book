# def output_result(result, log = None):
#     if log is not None:
#         log.debug('Got: %r', result)
# # Функция-пример
# def add(x,y):
#     return x + y
# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial
#
#     logging.basicConfig(level = logging.DEBUG)
#     log = logging.getLogger('test')
#     p = Pool()
#     p.apply_async(add(3,10),callback=partial(output_result,log = log))
#     p.close()
#     p.join()
#     print(p)

from socketserver import StreamRequestHandler, TCPServer
class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b'GOT:'+ line)
serv = TCPServer(('',1500),EchoHandler)
print(serv.serve_forever())
