import socket

ip_address = '0.0.0.0'
port = 8585
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip_address, port))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from: ", client_address)
    data = client_socket.recv(1024).decode()
    print("Needle: ", data)
    client_socket.close()