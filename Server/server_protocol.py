import socket
import threading


class UDP_Server:
    # Method to initialize the server with a host and port
    def __init__(self, host, port):
        self.host_ip = host # The host IP address
        self.host_port = port # The host port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using IPv4 and UDP

    # Method to start the server
    def create_socket(self):
        self.socket.bind((self.host_ip, self.host_port)) # Binds the socket to the local host and port, ready to receive data
        print(f"Server started on {self.host_ip}:{self.host_port}")

    # Method to receive messages
    def receive_message(self):
        while True:
            data = self.socket.recvfrom(1024)
            data = data[0].decode()
            print(f"\nUnknown: {data}")

    # Method to send messages
    def send_message(self):
        while True:
            message = input("You: ") # Enter a message
            self.socket.sendto(message.encode(), (self.host_ip, self.host_port))

    receive = threading.Thread(target=receive_message)
    send = threading.Thread(target=send_message)

    receive.start()
    send.start()

    
if __name__ == "__main__":
    server = UDP_Server("127.0.0.1", 5000)
    server.create_socket()