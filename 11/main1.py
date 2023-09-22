import socket


def tcp_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('localhost', 8080))

    # Listen for incoming connections (max 5 clients in the waiting queue)
    server_socket.listen(5)
    print("Server started, waiting for connections...")

    while True:
        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")

        client_socket.sendall(data)
        client_socket.close()


if __name__ == '__main__':
    tcp_server()
