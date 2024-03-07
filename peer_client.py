import socket
import threading


class UDP_Client:
    # Method to initialize the server with a host and port
    def __init__(self, host, port):
        self.client_ip = host # The host IP address
        self.client_port = port # The host port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Using IPv4 and UDP

    # Socket does not need to be bound to the local host and port, as it is not receiving data

    # Method to send messages
    def send_message(self):
        while True:
            message = input("You: ") # Enter a message
            self.socket.sendto(message.encode(), (self.client_ip, self.client_port))

    # Method to receive messages
    def receive_message(self):
        while True:
            data = self.socket.recvfrom(1024)
            data = data[0].decode()
            print(f"\nUnknown: {data}")

    # Method to start the threads
    def start_threads(self): 
        receive = threading.Thread(target=self.receive_message)
        send = threading.Thread(target=self.send_message)

        receive.start()
        send.start()

    
if __name__ == "__client_protocol__":
    server = UDP_Client("127.0.0.1", 5000)
    server.start_threads()