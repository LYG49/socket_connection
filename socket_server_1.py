
import socket

host = '0.0.0.0'
port = 3360

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()

img_data = b''
# print(img_data)
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    img_data += data
    print(data)
    print(img_data)
with open('received_image.jpg', 'wb') as f:
    f.write(img_data)

client_socket.close()
# server_socket.close()
