from urllib import request,parse
# Базовый URL, к которому обращаемся
url = 'http://httpbin.org/get'
# Словарь параметров запроса (если они есть)
parms = {
    'name1' : 'value1',
    'name2' : 'value2',
}
# Кодируем строку запроса
querystring = parse.urlencode(parms)
# Делаем GET-запрос и читаем ответ
u = request.urlopen(url + '?' + querystring)
resp = u.read()
print(resp)