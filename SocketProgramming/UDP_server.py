from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))  # '' allows it to listen on all interfaces
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(f"Received message: {message.decode()} from {clientAddress}")
    modifiedMessage = message.decode().upper()  # Convert to uppercase
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)