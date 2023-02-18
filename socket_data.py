import socket



host = '192.168.137.23'
port = 3306
address = (host,port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        #定義IPV4、TCP協定
s.connect(address)                                           #取得IP,PORT
with open ("C:/Users/user/yolov7/result.txt" ,"r") as f:                                 #開啟txt檔案
    content = f.read()                                                #讀取
    readlines = content.split(":")                                    #用:做為斷點
    for line in readlines:                                            #將資料用for迴圈撈出來
        print(line) 
text_data = line                                                    #將取得的值存入text_data
s.sendall(text_data.encode())                                #傳輸
s.close() 