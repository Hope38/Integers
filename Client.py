import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("before s.connect")
    s.connect((HOST, PORT))
    print("after s.connect")
    while True:
        choice = input('Enter your choice (rock, paper, or scissors): ')
        s.sendall(choice.encode())
        print("after s.sendall choice=" + choice)
        result = s.recv(1024).decode()
        print("after s.recv result=" + result)
