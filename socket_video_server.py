#####################################################導入函式庫######################################################

import socket
import cv2
import pickle
import struct 

###################################################建立socket連線####################################################

host='0.0.0.0'
port=3360
socket_video_server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_video_server.bind((host,port))
socket_video_server.listen(10)
conn,addr=socket_video_server.accept()

########################################################導入函式庫###################################################

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        data += conn.recv(4096)
        if not data:
            cv2.destroyAllWindows()
            conn,addr=socket_video_server.accept()
            continue
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:] 
    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('server',frame)
    cv2.waitKey(1)