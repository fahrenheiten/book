from socket import socket,AF_INET,SOCK_STREAM
import threading
class LazyConnection:
    def __init__(self,adress,family = AF_INET,type = SOCK_STREAM):
        self.adress = adress
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()
    def __enter__(self):
        if hasattr(self.local,'soks'):
            raise RuntimeError('Already connection')
        self.local.sock = socket(self.family,self.type)
        self.local.sock.connect(self.adress)
        return self.local.sock
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock
from functools import partial
def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
    print('Got {} bytes'.format(len(resp)))
if __name__ == '__main__':
    conn = LazyConnection(('www.python.org',80))
    t1 = threading.Thread(target=test,args=(conn,))
    t2 = threading.Thread(target=test,args=(conn,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

