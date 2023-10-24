import socket

class UDP:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Server address and port
        self.server_address = ('localhost', 7500)

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.server_socket.bind(('127.0.0.1', 7501))  # Uncomment this line if needed

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

# Uncomment the following lines if you need to run the server
# udp_server = UDP()
# udp_server.server()
