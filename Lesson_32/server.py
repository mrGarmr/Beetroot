import socket

HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
    server_socket.bind((HOST, PORT))
    print(f"UDP server is listening on {HOST}:{PORT}")

    while True:
        data, addr = server_socket.recvfrom(1024)  # Receive data
        print(f"Received from {addr}: {data.decode()}")
        
        response = data.upper()  # Convert to uppercase
        server_socket.sendto(response, addr)  # Send response
