# from socket import socket,AF_INET,SOCK_STREAM
# import ssl
# import os
# KEYFILE = 'server_key.pem'# Приватный ключ сервера
# CERTFILE = 'server_cert.pem'# Сертификат сервера (передаваемый клиенту)
#
# def echo_client(s):
#     while True:
#         data = s.recv(8192)
#         if data == b'':
#             break
#         s.send(data)
#     s.close()
#     print('Connection closed')
# def echo_server(address):
#     s = socket(AF_INET,SOCK_STREAM)
#     s.bind(address)
#     s.listen(1)
#     # Оборачивает слоем SSL, требуя клиентских сертификатов
#     s_ssl = ssl.wrap_socket(s,
#                             keyfile=KEYFILE,
#                             certfile=CERTFILE,
#                             server_side=True)
#     # Ждет соединений
#     while True:
#         try:
#             c,a = s_ssl.accept()
#             print('Got connection', c, a)
#             echo_client(c)
#         except Exception as e:
#             print('{}: {}'.format(e.__class__.__name__, e))
# echo_server(('',20000))
# try:
#     with open('C:\\Users\\CPSP-USER\\PycharmProjects\\book\\11\\11.10\\11.10.1.py', 'r') as f:
#         content = f.read()
#         print(content)
# # File operations
# except FileNotFoundError:
#     print('File not found')

