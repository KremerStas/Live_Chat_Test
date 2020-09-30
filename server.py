import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 5080))
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
