filename = 'spam.txt'
filename1 = filename.endswith('txt')
filename2 = filename.startswith('spam')
url = 'http://www.python.org'
url = url.startswith('http:')
print(filename1)
print(filename2)
print(url)
filename = 'spam.txt'
print(filename[-4] == '.txt')