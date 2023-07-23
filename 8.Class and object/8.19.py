class Connection:
    def __init__(self):
        self.new_state(ClosedConnectionState)
    def new_state(self,newstate):
        self._state = newstate
    '''Делигируем классу состояния'''
    def read(self):
        return self._state.read(self)
    def write(self,data):
        return self._state.write(self,data)
    def open(self):
        return self._state.open(self)
    def closed(self):
        return self._state.closed(self)
    '''Базовый класс состояния соединения'''
class ConnectionState:
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    @staticmethod
    def write(conn,data):
        raise RuntimeError('Not open')
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    @staticmethod
    def close(conn):
        raise RuntimeError('Already cllosed')
    '''Реализация различных состояний'''
class ClosedConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        raise RuntimeError('Not open')
    @staticmethod
    def write(conn,data):
        raise RuntimeError('Not open')
    @staticmethod
    def open(conn):
        conn.new_state(OpenConnectionState)
    @staticmethod
    def close(conn):
        raise RuntimeError('Already closed')
class OpenConnectionState(ConnectionState):
    @staticmethod
    def read(conn):
        print('reading')
    @staticmethod
    def write(conn,data):
        print('writing')
    @staticmethod
    def open(conn):
        raise RuntimeError('Already open')
    @staticmethod
    def close(conn):
        conn.new_state(ClosedConnectionState)
c = Connection()
c._state
c.open()
print(c._state)
print(c.read())
print(c.close())