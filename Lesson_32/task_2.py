# Extend the echo server, which returns to client the data, 
# encrypted using the Caesar cipher algorithm by a specific key obtained from the client.

import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def caeser_cipher(key,data):
    data_ascii = [ord(ch) for ch in data]
    cipher_data_ascii = [ch+key for ch in data_ascii]
    caesar_cipher = ''.join([chr(ch) for ch in cipher_data_ascii])
    
    return caesar_cipher


# _______________SERVER__________________
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data, key = conn.recv(1024).split('###')

            if not data:
                break
            conn.sendall(caeser_cipher(key, data))


def decoder_caeser_cipher(key,data):
    data_ascii = [ord(ch) for ch in data]
    cipher_data_ascii = [ch-key for ch in data_ascii]
    clear_data = ''.join([chr(ch) for ch in cipher_data_ascii])

    return clear_data

#______________CLIENT______________

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = input("Please input your message: ")
    key = int(input("Please input key: "))
    s.sendall(f"{data}###{key}")
    data = s.recv(1024)

print('Received', decoder_caeser_cipher(key, data))