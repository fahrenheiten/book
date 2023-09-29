class NetworkError(Exception):
    pass
class HostnameError(NetworkError):
    pass
class TimeoutError(NetworkError):
    pass
class ProtocolError(NetworkError):
    pass
try:
    raise RuntimeError('It failed')
except RuntimeError as e:
    print(e.args)
try:
    raise RuntimeError('It failed',42,'spam')
except RuntimeError as e:
    print(e.args)
class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status