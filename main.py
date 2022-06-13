import socket


# Подаем данные в формате BBBBxNNxHH:MM:SS.zhqxGGCR
def strip(line):
    new = 'Спортсмен, нагрудный номер {player_num}' \
          ' прошёл отсечку {channel_id}' \
          ' в {hours}:{minutes}:{seconds}.{millisec}'.format(player_num=line[0:4],
                                                             channel_id=line[5:7],
                                                             hours=line[8:10],
                                                             minutes=line[11:13],
                                                             seconds=line[14:16],
                                                             millisec=line[17])
    return new

# Адрес сервера
IP = socket.gethostbyname(socket.gethostname())
PORT = 8686
SERVER_ADDRESS = (IP, PORT)

# Настраиваем сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(5)
print('Server is running')

# Слушаем запросы
while True:
    connection, address = server_socket.accept()
    print("New connection from {address}".format(address=address))
    data = connection.recv(1024).decode('UTF-8')
    logs = open("logs.txt", 'a') #Запись сообщения
    logs.write(data)
    logs.close()
    if data[21:23] == '00':  # Проверяем на принадлежность к группе 00
        print(strip(data))
    connection.send(bytes('Information collected', encoding='UTF-8'))
    connection.close()
