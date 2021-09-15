import os
from socket import *
import subprocess
import time


port = 12502
Server= socket(AF_INET,SOCK_STREAM) # Definindo a versão do IP  e o protocolo de transporte
Server.bind(("",port)) #Ligamos o socket ao endereço que solicitou a conexão. Nesse caso a porta listening é 12501 e o ip é qualquer.
Server.listen(5) # Enable a server to accept connections. o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão 
print("Waiting...")
connectionSocket, addr = Server.accept() #ACeita a connection
print("Connection established \n")

while True:   
    print("Waiting for command...")
    Receive = connectionSocket.recv(4096,) #Recebe em bytes
    Received = Receive.decode(encoding='utf-8') #Decodificar
    print ("Received From Client: ", Received)
   
    Command = subprocess.run(shell=True, args=Received)
    subprocess.CompletedProcess(args=[Received], returncode=0)
    print(Command)
   
    if Received == "sair":
        print("Closed connection")
        Server.close() #close connection
        break    

    if "returncode=1" in str(Command):
        print("Erro")
        connectionSocket.sendall("Comando inválido".encode(encoding='utf-8'))

    elif "returncode=0" in str(Command):
        Command = os.popen(Received).read()#Abre uma shell- Converter uma sequência de argumentos em uma string no Windows e armazena na variavel
        if Command == "":
            print("Received em 0")
            connectionSocket.sendall("Sucesseful".encode(encoding='utf-8'))

        else:
            print("Sucesso",Command)
            #Command = os.popen(Received).read();  
            connectionSocket.sendall(Command.encode(encoding='utf-8'))#Envia o resultado do comando executado na shell em forma de bytes
        