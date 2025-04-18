from socket import *

serverName = 'localhost'  # Use '127.0.0.1' if running both client and server on the same machine
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence: ')  # Use input() in Python 3
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("From Server:", modifiedMessage.decode())
clientSocket.close()