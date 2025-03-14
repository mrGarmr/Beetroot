# Extend the echo server, which returns to client the data, 
# encrypted using the Caesar cipher algorithm by a specific key obtained from the client.

import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

def caeser_cipher(key,data):
    data_ascii = [ord(ch) for ch in data]
    cipher_data_ascii = [ch+int(key) for ch in data_ascii]
    caesar_cipher = ''.join([chr(int(ch)) for ch in cipher_data_ascii])
    
    return caesar_cipher


# _______________SERVER__________________
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print('SERVER STARTED!\n')
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        
        print('Connected by', addr)
        while True:
            data, _ = conn.recvfrom(1024)
            if not data:
                break
            print(data)
            message, key = data.decode().rsplit(':',1)
            print(message, key)
            cipher_message = caeser_cipher(key, message)
            conn.sendall(cipher_message.encode())
            
