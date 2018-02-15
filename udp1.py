import socket

host="127.0.0.1"
port=12346
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind((host,port))
    s.settimeout(5)
    data,addr=s.recvfrom(1024)
    print "received from ",addr
    print "obtained ",data
    s.close()
except socket.timeout:
    print"Client not connected"
    s.close()