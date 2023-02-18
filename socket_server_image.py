#####################################################導入函式庫######################################################

import socket

###################################################建立socket連線####################################################

host = '0.0.0.0'
port = 3360
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
client_socket, client_address = server_socket.accept()

######################################################接收圖片#######################################################

img_data = b''                                                              #解碼
while True:
    data = client_socket.recv(1024)                                         #接收
    if not data:
        break
    img_data += data
with open('received_image.jpg', 'wb') as f:                                 #開啟JPG檔寫入
    f.write(img_data)                                                       #將資料寫入進去

client_socket.close()
# server_socket.close()
