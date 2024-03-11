import threading
import socket
import ssl
import rsa

public_key, private_key = rsa.newkeys(1024)
public_Friend = None

context = ssl.create_default_context()
context.check_hostname = False  # Disable for development (not secure)

ip_address = socket.gethostbyname(socket.gethostname())

print(f"Server started on IP: {ip_address} Port: 5000")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_address, 5000))
server.listen()

client, _ = server.accept()
wrapped_client = context.wrap_socket(client, server_side=True)
wrapped_client.send(public_key.save_pkcs1("PEM"))
public_Friend = rsa.PublicKey.load_pkcs1(wrapped_client.recv(1024))


def send(wrapped_client):
    while True:
        message = input("You: ")
        wrapped_client.send(rsa.encrypt(message.encode(), public_Friend))


def receive(wrapped_client):
    while True:
        encrypted_message = wrapped_client.recv(1024)
        message = rsa.decrypt(encrypted_message, private_key).decode()
        print("\nFriend: " + message)


print("Start chatting!\n")


threading.Thread(target=send, args=(wrapped_client,)).start()
threading.Thread(target=receive, args=(wrapped_client,)).start()
