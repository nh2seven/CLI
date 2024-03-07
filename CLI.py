import server_protocol
import client_protocol
import threading

class CLI:
    def assign_role(self):
        print("1. Register this system as a server")
        print("2. Connect to an existing server as a client")
        end_system = input()

        # if end_system == "1":
                # to implement
            # while True:
                # server_protocol modules
                # server = threading.Thread(target=server_protocol)
                # server.start()
        # elif end_system == "2":
            # while True:
                # client_protocol
                # client = threading.Thread(target=client_protocol)
                # client.start()
        # else:
        #     print("Invalid input. Please try again.")
        #     self.assign_role()


if __name__ == "__main__":
    cli = CLI()
    # implement threading here
    # remove threads from client_protocol.py and server_protocol.py
