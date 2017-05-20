import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen(10)
while 1:
    conn, addr = s.accept()
    a = conn.recv(1024)
    print a
    conn.send(a)

