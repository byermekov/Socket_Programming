from socket import *


class Info:
    # Class for printing out info
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def postInfo(self, reply):
        send = "OK" if reply == "server: OK" else "ERROR"
        print("IP address: {}, Port Number: {}\nCommand: POST\nConnect Status: OK \nSend Status:{}".format(self.ip,
                                                                                                           self.port,
                                                                                                           send))

    def readInfo(self, reply):
        receive = "ERROR" if reply == "server: ERROR - Command not understood" else "OK"
        print(
            "IP address: {}, Port Number: {}\nCommand: READ\nConnect Status: OK \nReceive Status:{}\nResponse:".format(
                self.ip,
                self.port,
                receive))

    def connected(self):
        print("TCP connection successfully established")

    def initialized(self):
        print("TCP socket successfully created and initialized")

    def closed(self):
        print("TCP socket successfully closed")


serverName = input("Input the IP address of the server: ")
serverPort = int(input("Input the port number of the server: "))
info = Info(serverName, serverPort)

clientSocket = socket(AF_INET, SOCK_STREAM)
info.initialized()
clientSocket.connect((serverName, serverPort))  # Raises error if connection fails
info.connected()

command = ""
line = ""

while command != "QUIT":
    command = input("Input your command and press Enter to send it to the server: ")
    clientSocket.send(command.encode())

    while command == "POST" and line != "#":
        # take input line by line
        line = input()
        clientSocket.send(line.encode())
    line = ""  # reset the line so that above loop runs for the next POST command

    response = clientSocket.recv(4096).decode()
    if command == "POST":
        info.postInfo(response)
    elif command == "READ":
        info.readInfo(response)
        print(response)
    elif command not in ["READ", "POST"]:
        # if QUIT or other command
        print(response)

    while command == "READ" and response != "server: #":
        # print server response line by line
        response = clientSocket.recv(4096).decode()
        print(response)

# Close socket
clientSocket.close()
info.closed()
