import socket 
import sys


HOST = '127.0.0.1'
PORT = 60001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) #conecta com servidor

s.sendall(b'Hello, servidor!') #manda mensagem para o servidor
data = s.recv(1024) #recebe resposta do servidor
print(f"Recebido: {data.decode()}")#mostra a resposta
s.close() #fecha a conexao