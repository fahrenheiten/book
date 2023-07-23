from socket import socket, AF_INET,SOCK_STREAM
from functools import partial

class LazyConnection:
    def __init__(self,adress,family = AF_INET,type = SOCK_STREAM):
        self.adress = adress
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family,self.type)
        self.sock.connect(self.adress)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None
conn = LazyConnection(('https://www.python.org',80))
with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))
