import socket

class UDP:
    def __init__(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Server address and port
        server_address = ('localhost', 7500)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind('127.0.0.1', 7501)

    def client(self):
        while True:
            message = input("Enter a message to send to the server (or 'exit' to quit): ")
        
            if message.lower() == 'exit':
                break
    
        # Send the message to the server
        self.client_socket.sendto(message.encode(), self.server_address)

        # Close the socket
        self.client_socket.close()

    def server(self):
        while True:
            # Receive data from the client
            data, client_address = self.server_socket.recvfrom(1024)  # 1024 is the buffer size
            print(f"Received data from {client_address}: {data.decode()}")

        # Close the socket (not reached for now)
        self.server_socket.close()
