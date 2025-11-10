import socket 
import sys

HOST = 'localhost'
PORT = 60001
BUFFER_SIZE = 1024

#af_inet = ENDERECO IPV4
#SOCK_STREAM = TCP
#SOCKET_DGRAM = UDP 
# Create a TCP/IP socket 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#VINCULA A PORTA COM ENDERECO IP
s.bind((HOST, PORT))

#MODO ESCUTA
s.listen(1)
print (f"Aguardando conexao na porta {PORT}")
#ACEITA A CONEXAO
conn, addr = s.accept()
print(f"Conectado por {addr}")

#LOOP DE RECEPCAO DE DADOS
while True:
    #recebe DADOS com BUFFER_SIZE ( tamnho maximo de bytes  )
    data = conn.recv(BUFFER_SIZE)
    if not data:
        print("Conexao encerrada pelo cliente")
        conn.close()
        break
    
    print(f"Recebido: {data.decode()}")
    conn.sendall(data)  #ECOA OS DADOS RECEBIDOS