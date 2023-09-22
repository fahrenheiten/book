import socket

def tcp_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the server's address and port
    client_socket.connect(('localhost', 8080))

    message = "Hello, Server!"
    client_socket.sendall(message.encode('utf-8'))

    data = client_socket.recv(1024)
    print(f"Received: {data.decode('utf-8')}")

    client_socket.close()

if __name__ == '__main__':
    tcp_client()
