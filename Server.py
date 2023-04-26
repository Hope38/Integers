import socket
import random

HOST = '127.0.0.1'
PORT = 65432

options = ['rock', 'paper', 'scissors']

def play_game(player_choice):
    server_choice = random.choice(options)
    print("server_choice=" + server_choice)

    if player_choice == server_choice:
        return 'Tie', server_choice
    elif player_choice == 'rock' and server_choice == 'scissors':
        return 'Player wins!', server_choice
    elif player_choice == 'paper' and server_choice == 'rock':
        return 'Player wins!', server_choice
    elif player_choice == 'scissors' and server_choice == 'paper':
        return 'Player wins!', server_choice
    else:
        return 'Server wins!', server_choice

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("before s.bind")
    s.bind((HOST, PORT))
    print("after s.bind, before s.listen")
    s.listen()
    print(f'Server is listening on {HOST}:{PORT}')

    conn, addr = s.accept()
    print("after accept, conn=" + str(conn) + ", addr=" + str(addr))
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            print("after conn.recv")
            if not data:
                break

            player_choice = data.decode()
            print(f'Player chose {player_choice}')

            result, server_choice = play_game(player_choice)
            conn.sendall((result + " (Server chose " + server_choice + ")").encode())        
            print("After conn.sendall and result=" + result)
