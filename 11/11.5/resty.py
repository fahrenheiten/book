import cgi

def notfound_404(environ, start_response):
    start_response('404 Not Found', [ ('Content-type', 'text/plain') ])
    return [b'Not Found']
class PathDispatcher:
    def __init__(self):
        self.pathmap = {}

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        params = cgi.FieldStorage(environ['wsgi.input'],
                              environ=environ)
        method = environ['REQUEST_METHOD'].lower()
        environ['params'] = {key: params.getvalue(key) for key in params}
        handler = self.pathmap.get((method, path), notfound_404)
        return handler(environ, start_response)
def rigister(self, method, path, function):
    self.pathmap[method.lower(), path] = function
    return function
import time
_hello_resp = '''\
<html>
<head>
<title>Hello {name}</title>
</head>
<body>
<h1>Hello {name}!</h1>
</body>
</html>'''