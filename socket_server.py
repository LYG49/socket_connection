#####################################################導入函式庫######################################################

import socket

###################################################建立socket連線####################################################

host = '0.0.0.0'
port = 3306
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)

####################################################接收文字訊息#####################################################

while True:
    client_socket, client_address = server_socket.accept()
    print("Accepted connection from: ", client_address)
    data = client_socket.recv(1024).decode()
    print("content: ", data)
    client_socket.close()
