import socket


def echo_client():
    host = 'localhost'
    port = 20000

    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((host, port))

    # Send data
    message = "Hello, Echo Server!"
    s.sendall(message.encode('utf-8'))

    # Receive the echoed data
    data = s.recv(1024)
    print("Received:", data.decode('utf-8'))

    # Close the socket
    s.close()


if __name__ == "__main__":
    echo_client()
