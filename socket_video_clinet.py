############################################################導入函式庫################################################################

import cv2
import socket
import struct
import pickle

##########################################################建立socket連線##############################################################

host = "192.168.50.22"
post = 3360
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, post))

########################################################開啟鏡頭和參數設定##############################################################

cam = cv2.VideoCapture(0)
# encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
encode_param=[cv2.IMWRITE_JPEG_QUALITY,90]                                  #將影像以壓縮成jpg的形式,後者為壓縮比例的參數0到100

#####################################################################################################################################

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,180)
    result, image = cv2.imencode('.jpg', frame, encode_param)
    data = pickle.dumps(image, 0)
    size = len(data)
    client_socket.sendall(struct.pack(">L", size) + data)
    # cv2.imshow('client',frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    
