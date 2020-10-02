## About Live Chat

- Live Chat создан с помощью стандарных библиотек Python:
    - socket
    - threading
    - datetime
    - configparser
- Live Chat реализует общение между пользователями через сервер, в данном тестовом варианте - через локальный сервер (127.0.0.1, 5080)


## About Applications server and client

Для использования чата на Windows без Python были созданы файлы client и server.
Файлы храняться в папке 'applications' и имеют формат .exe

PS:
    Использована сторонняя библиотека для компиляции файлов (PyInstaller)
    
## Start Live Chat

Для старта программы запускаются файлы server.exe и client.exe, которые находятся в папке application.
Там же есть файл settings с конфигурациями, чтобы поменять тестовый локальный сервер на удаленный.
