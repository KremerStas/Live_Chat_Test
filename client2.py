import socket
import threading
from datetime import datetime


class NewClient:
    def __init__(
            self, server=('127.0.0.1', 5080),
            nickname=input('Введите имя пользователя: '),
            sock=None,
            thread=None
    ):
        self.server = server
        self.nickname = nickname
        self.sock = sock
        self.thread = thread

    def read_socket(self):
        while True:
            try:
                data = self.sock.recv(1024)
                print(data.decode('utf-8'))
            except:
                break

    def create_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', 0))
        self.thread = threading.Thread(target=self.read_socket)
        self.thread.start()

    def start_send_message(self):
        self.sock.sendto((self.nickname + ' присоединился к чату').encode('utf-8'), self.server)
        print('Для выхода из чата введите: "$exit"')
        while True:
            our_time = datetime.now().strftime('%H:%M:%S')
            message = input()
            if message.upper() != '$EXIT':
                self.sock.sendto(('[' + self.nickname + ']' + '[' + our_time + ']' + message).encode('utf-8'),
                                 self.server)
            else:
                self.sock.sendto((self.nickname + ' выходит из чата').encode('utf-8'), self.server)
                break
        self.sock.close()


a = NewClient()
a.create_socket()
a.start_send_message()