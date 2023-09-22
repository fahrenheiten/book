from socket import socket, AF_INET, SOCK_STREAM
import ssl
s = socket(AF_INET,SOCK_STREAM)
s_ssl = ssl.wrap_socket(s,
                        cert_reqs=ssl.CERT_REQUIRED,
                        ca_certs='server_cert.per')
s_ssl.connect(('localhost',20000))
print(s_ssl.send(b'Hello World?'))