#####################################################導入函式庫######################################################

import socket

###################################################建立socket連線####################################################

host = '120.117.40.244'
port = 3306
address = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

######################################################資料傳輸#######################################################

print('start send image')
imgFile = open("2_7.jpg", "rb")
while True:
    imgData = imgFile.readline(1024)
    if not imgData:
        break
    s.send(imgData)
imgFile.close()
s.close()
