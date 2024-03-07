import socket
import threading


class UDP_Server:
    # Method to initialize the server with a host and port
    def __init__(self, host, port):
        self.server_ip = host # The host IP address
        self.server_port = port # The host port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using IPv4 and UDP

    # Method to start the server
    def create_socket(self):
        self.socket.bind((self.server_ip, self.server_port)) # Binds the socket to the local host and port, ready to receive data
        print(f"Server started on {self.server_ip}")
        print(f"Server listening on port {self.server_port}")

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
            if message == "!q": # vim-style quit command
                self.socket.sendto("!q".encode(), (self.server_ip, self.server_port))
                print("Server shutting down...")
                self.socket.close()
                break
            self.socket.sendto(message.encode(), (self.server_ip, self.server_port))

    # Method to start the threads
    def start_threads(self): 
        receive = threading.Thread(target=self.receive_message)
        send = threading.Thread(target=self.send_message)

        receive.start()
        send.start()


ip_address = socket.gethostbyname(socket.gethostname())

if __name__ == "__server_protocol__":
    server = UDP_Server(ip_address, 5000)
    server.create_socket()
    server.start_threads()