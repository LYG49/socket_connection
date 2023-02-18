import socket

host = '120.117.40.244'
port = 8082
address = (host,port)


socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket02.connect(address)



###########################################################################

#開始傳輸
print('start send image')
imgFile = open("2_7.jpg", "rb")

while True:
    imgData = imgFile.readline(1024)

    if not imgData:
        break
    socket02.send(imgData)
imgFile.close()
print('transmit end')
###########################################################################

socket02.close()
print('client close')