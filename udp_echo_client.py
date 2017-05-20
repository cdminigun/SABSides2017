import socket 
server = (('127.0.0.1', 1234))
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 0)) #OS decides port
s.sendto("hello", server)
data, addr = s.recvfrom(1024)
print data
