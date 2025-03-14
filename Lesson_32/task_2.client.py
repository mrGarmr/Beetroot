import socket

HOST = '127.0.0.1'  # Standard loop-back interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


def decoder_caeser_cipher(key,data):
    data_ascii = [ord(ch) for ch in data]
    cipher_data_ascii = [ch-key for ch in data_ascii]
    clear_data = ''.join([chr(ch) for ch in cipher_data_ascii])

    return clear_data

#______________CLIENT______________

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print('CLIENT STARTED!\n')
    data = input("Please input your message: ")
    key = int(input("Please input key: "))
    s.sendall(f"{data}:{key}".encode())
    encrypted_message, _ = s.recvfrom(1024)
    print(f"Encrypted response from server: {encrypted_message.decode()}")

