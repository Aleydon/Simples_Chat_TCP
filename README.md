# Simples_Chat_TCP
### Site para baixar o Ngrok: 
> https://ngrok.com/

##### Um chat simples cliente/servidor usando o Ngrok para conexão e Termux(Terminal Android)

```python

#-*-coding:utf-8-*-
import socket
from os import system


class ServidorChat(object):
   def __init__(self):
      self.titulo = system('figlet Servidor')
      self.ip     = input(str('\033[33mInsira o Ip do Servidor\033[m: '))
      self.port   = input(str('\033[33mInsira a porta do Servidor\033[m: '))
      self.limpar = system('clear')

   
   def Conectado(self):
      self.chat = system('cowsay "Chat On"')
      self.servidor  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.servidor.bind((self.ip, int(self.port)))
      self.servidor.listen(5)
      print('\033[33m\nAguardando cliente se conectar...\033[m')
      client_socket, address = self.servidor.accept()
      print('\n\033[36mConectado por\033[m ', address)
      system('termux-toast "Conexão estabelecida"')
      system('clear')
      while True:
         print('\033[34mAguardando resposta...')
         receber = client_socket.recv(2048)
         if not receber: 
            break
         print('\n\033[33mCliente\033[m: ', receber.decode('utf-8'))
         msg = input('\n\033[36mServidor\033[m: ')
         client_socket.send(msg.encode('utf-8'))
         system('termux-toast "Menssagem Enviada"')
         self.servidor.close()
      self.servidor.close()

```

### ScreenShot do servidor onde o ip e a porta o do Ngrok



![servertermux](https://user-images.githubusercontent.com/34782498/44436767-5af86480-a58d-11e8-85c3-d7f24eee4864.png)

> Acessando servidor com o ip e porta 

```python

# -*- coding:utf-8 -*-
import socket
from os import system



class ClientAcess(object):
   def __init__(self):
      self.titulo = system('figlet "Chat Client"')
      self.ip = input('\033[33mInsira o Ip do Servidor\033[m: ')
      self.port = input('\033[33mInsira a porta do Servidor\033[m: ')
      system('clear')
      

   def Conectado(self):
      system('cowsay "Chat On"')
      self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      self.cliente.connect((self.ip, int(self.port)))
      while True:
         msg = input('\n\033[36mCliente\033[m: ')
         self.cliente.send(msg.encode('utf-8'))
         system('termux-toast "Menssagem Enviada"')
         print('\033[34mAguardando resposta...')
         resposta = self.cliente.recv(2048)
         print('\n\033[33mServidor\033[m: ',resposta.decode('utf-8'))
         system('termux-toast "Conectado ao servidor"')
      self.cliente.close()
```

#### Envio de menssagem cliente para servidor.
![clientenviandomenssagem](https://user-images.githubusercontent.com/34782498/44437167-21285d80-a58f-11e8-8e77-2a3b3f4196e8.png)
