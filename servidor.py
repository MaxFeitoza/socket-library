import socket 
import sys

HOST = '127.0.0.1'
PORT = 6789
BUFFER_SIZE = 1024

#af_inet = ENDERECO IPV4
#SOCK_STREAM = TCP
#SOCKET_DGRAM = UDP 
# Create a TCP/IP socket 
serverSocket  = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cria o socket
#VINCULA A PORTA COM ENDERECO IP
serverSocket.bind((HOST, PORT))

#MODO ESCUTA
serverSocket.listen(1) #tamanho maximo de conexoes ( outros ficam na fila de espera )

#LOOP DE RECEPCAO DE DADOS
while True:
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept() #aceita a conexao do cliente
    try:
        message = connectionSocket.recv(BUFFER_SIZE).decode() #recebe mensagem do cliente com BUFFER_SIZE ( tamnho maximo de bytes  )
        filename = message.split()[1] 
        f = open(filename[1:]) 
        outputdata = f.readlines() #le o arquivo e retorna uma lista de linhas
        f.close()  # Fecha o arquivo
        
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode()) #envia os dados para o cliente "send"
        connectionSocket.send("\r\n".encode())
        
        # Fecha a conexão com o cliente após enviar o arquivo
        connectionSocket.close()
    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # Fecha o socket do cliente
        connectionSocket.close()
        break # Nao e necessario continuar o loop se o arquivo nao for encontrado 

serverSocket.close()
sys.exit() #encerra o programa

