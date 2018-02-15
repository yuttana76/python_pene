import socket
host="127.0.0.1" 
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(2)
conn, addr = s.accept()
print addr,"Now Connected"
conn.send("Thank you for connecting x1")
conn.close()