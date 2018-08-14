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
  