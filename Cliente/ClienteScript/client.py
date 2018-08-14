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

