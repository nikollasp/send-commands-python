import os
from socket import *

    

def automatic():
    print("ddddd")

def remote():
   
    while (True):
        Command = input(str("Input: "))
        while Command == "":
            print("Type a command: ")
            Command = input(str("Input: "))
    
        SockCli.sendall(Command.encode(encoding='utf-8')) 
        Receive = SockCli.recv(4096)
        Received=Receive.decode(encoding='utf-8')
        print(Received)
   

        if Command == "sair":
            print("Closed connection")
            SockCli.sendall(Command.encode(encoding='utf-8')) 
            SockCli.close() #Encerra o socket
            break

address = "localhost"
port = 12502
SockCli = socket(AF_INET, SOCK_STREAM) #Defnição do protocolo IPv4 e o transporte protocolo TCP que será usado para transmissão
SockCli.connect ((address,port)) #Conecta ao endereço e a porta informada
#Command = os.system('echo %cd%') #Abre uma subshell no sistema e retorna o comando especificado 

choice=input("Escolha 1-para Remote Access ou 2-automatic execution: ")
print(choice)
if choice == "1":
    print(choice)
    remote()
else:
    automatic()
