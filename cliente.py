import socket 
import sys


HOST = '127.0.0.1'
PORT = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.sendall(b'Hello, servidor!')
data = s.recv(1024)
print(f"Recebido: {data.decode()}")
s.close()