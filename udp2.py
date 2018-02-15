import socket
host="127.0.0.1"
port=12346
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print s.sendto("hello allx",(host,port))
s.close()