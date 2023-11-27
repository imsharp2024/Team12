import socket

class UDP:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Server address and port for broadcasting
        self.broadcast_address = ('localhost', 7500)

        # Server address and port for receiving
        self.receive_address = ('localhost', 7501)
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(self.receive_address)

    def client(self, message):
        # Send the message to the server for broadcasting
        self.client_socket.sendto(message.encode(), self.broadcast_address)

    def server(self):
        while True:
            # Receive data from the client
            data, client_address = self.server_socket.recvfrom(1024)  # 1024 is the buffer size
            received_data = data.decode()

            # Process received data
            self.process_received_data(received_data)

    def process_received_data(self, received_data):
        # Split received data into components
        components = received_data.split(':')

        if len(components) == 1:
            # Single integer (equipment id of the player who got hit)
            equipment_id = components[0]
            # Process the equipment id (e.g., handle scoring, check for friendly fire)
            self.process_hit(equipment_id)

        elif len(components) == 2:
            # Format: integer:integer (equipment id of player transmitting:equipment id of player hit)
            transmitter_id, receiver_id = components
            # Process the received data (e.g., transmit equipment id, handle base scoring)
            self.process_received_game_data(transmitter_id, receiver_id)

    def process_hit(self, hit_data):
        # Split the received data into equipment ids
        hit_player, hitter_player = map(int, hit_data.split(':'))

        # Check if the hitter is hitting a teammate
        if hit_player == hitter_player:
            # Transmit the equipment id of the hitter
            self.client_socket.sendto(str(hitter_player).encode(), self.broadcast_address)
        else:
            # Transmit the equipment id of the player that was hit
            self.client_socket.sendto(str(hit_player).encode(), self.broadcast_address)

            # Check if the hit was on a base and set the flag
            if hit_player in [53, 43]:  # Replace with the actual equipment id for bases
                # Transmit the flag to the player who hit the base
                self.client_socket.sendto('hit_base'.encode(), self.broadcast_address)

                # Find the player in the team and set the 'hit_base' flag to True
                for player_info in self.red_team_players + self.green_team_players:
                    if player_info['equipment_id'] == hitter_player:
                        player_info['hit_base'] = True

    def process_received_game_data(self, transmitter_id, receiver_id):
        # Handle logic for processing game-related data
        if transmitter_id == "202":
            # Game start signal
            print("Game started!")

        elif receiver_id == "221":
            # Game end signal
            print("Game ended!")

        elif transmitter_id == "53":
            # Red base scored
            print("Red base scored!")

        elif transmitter_id == "43":
            # Green base scored
            print("Green base scored!")

        else:
            # Handle other game-related data as needed
            pass
