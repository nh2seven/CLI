import threading
import socket

import rsa

public_key, private_key = rsa.newkeys(1024)
public_Friend = None

choice = input("Enter (1) to be Host or (2) to connect:  ")

if choice == "1":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 9998))
    server.listen()

    client, _ = server.accept()
    client.send(public_key.save_pkcs1("PEM"))
    public_Friend = rsa.PublicKey.load_pkcs1(client.recv(1024))

elif choice == "2":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9998))
    public_Friend = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))

else:
    exit()


def send(client):
    while True:
        message = input("You: ")
        client.send(rsa.encrypt(message.encode(), public_Friend))
        # client.send(message.encode())


def receive(client):
    while True:
        encrypted_message = client.recv(1024)
        message = rsa.decrypt(encrypted_message, private_key).decode()
        print("\nFriend: " + message)
        # print("\nFriend: " + encrypted_message.decode())


print("Start chatting!\n")


threading.Thread(target=send, args=(client,)).start()
threading.Thread(target=receive, args=(client,)).start()
