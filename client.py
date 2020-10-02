import socket
import threading
from datetime import datetime
from config import load_config


config = load_config()
ip = config[0]
port = int(config[1])


class NewClient:
    def __init__(
            self, server=(ip, port),
            nickname=input('Введите имя пользователя: '),
            sock=None,
            thread=None
    ):
        while not nickname.strip():
            print('Введите имя, содержащее символы')
            nickname = input('Введите имя пользователя: ')
        self.server = server
        self.nickname = nickname
        self.sock = sock
        self.thread = thread

    def read_socket(self):
        while True:
            try:
                data = self.sock.recv(1024)
                print(data.decode('utf-8'))
            except OSError:
                break

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 0))
        self.thread = threading.Thread(target=self.read_socket)
        self.thread.start()

    def start_send_message(self):
        self.sock.sendto(f'{self.nickname} присоединился к чату'.encode('utf-8'), self.server)
        print('Для выхода из чата введите: "$exit"')
        while True:
            our_time = datetime.now().strftime('%H:%M:%S')
            message = input()
            if message.upper() == '$EXIT':
                self.sock.sendto(f'{self.nickname} выходит из чата'.encode('utf-8'), self.server)
                break
            elif not message.strip():
                continue
            else:
                self.sock.sendto(f'[{self.nickname}][{our_time}]{message}'.encode('utf-8'),
                                 self.server)
        self.sock.close()


a = NewClient()
a.create_socket()
a.start_send_message()