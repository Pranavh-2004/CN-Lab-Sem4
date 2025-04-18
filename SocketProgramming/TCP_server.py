from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))  # '' allows it to listen on all interfaces
serverSocket.listen(1)  # Server listens for 1 connection at a time
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()  # Accept a client connection
    print(f"Connected to: {addr}")  # Print client's address
    
    sentence = connectionSocket.recv(1024).decode()  # Receive data from client
    print(f"Received: {sentence}")
    
    capitalizedSentence = sentence.upper()  # Convert the sentence to uppercase
    connectionSocket.send(capitalizedSentence.encode())  # Send back the modified sentence
    
    connectionSocket.close()  # Close the connection