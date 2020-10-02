import socket
from config import load_config


config = load_config()
ip = config[0]
port = int(config[1])

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, port))
    client = []  # Массив c адресами клиентов
    print('Live Chat запущен')
    while True:
        data, address = sock.recvfrom(1024)
        print(address)
        if address not in client:
            client.append(address)
        for clients in client:
            if clients == address:
                continue  # Не отправлять сообщение клиенту, который их прислал
            sock.sendto(data, clients)
except OSError:
    print('Проверьте правильность ввода данных конфигурации')
