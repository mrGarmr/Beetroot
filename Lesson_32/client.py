import socket

HOST = '127.0.0.1'  # Server's IP address
PORT = 65432        # Server's port

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
    message = b'Hello, world'
    
    # Send data to server
    client_socket.sendto(message, (HOST, PORT))
    
    # Receive response from server
    data, _ = client_socket.recvfrom(1024)
    print("Received:", data.decode())
