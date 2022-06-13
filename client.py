#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import random as rd
from datetime import datetime

MAX_CONNECTIONS = 2
IP = socket.gethostbyname(socket.gethostname())
PORT = 8686
server_address = (IP, PORT)
clients = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for i in range(MAX_CONNECTIONS)]
for client in clients: #Создаем искусственные запросы\клиенты к серверу
    client.connect(server_address)

#Создаем рандомные сообщения от клиентов в соответствии с указанным форматом для теста сервера
for i in range(MAX_CONNECTIONS):
    time = str(datetime.time(datetime.now()))[:12]
    message_data = (rd.randint(1000,9999), rd.randint(10,99), time,  rd.choice(('00', '01')))
    message = '{0} {1} {2} {3}\r'.format(*message_data)
    clients[i].send(bytes(message, encoding='UTF-8'))

for client in clients:
    data = client.recv(1024)
    print(str(data))

