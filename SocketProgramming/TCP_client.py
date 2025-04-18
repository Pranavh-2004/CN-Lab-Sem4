from socket import *
serverName = 'localhost'  # Use '127.0.0.1' if running on the same machine
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))  # Connect to the server

sentence = input('Input lowercase sentence: ')  # Prompt the user for input
clientSocket.send(sentence.encode())  # Send the input to the server

modifiedSentence = clientSocket.recv(1024).decode()  # Receive the response
print('From Server:', modifiedSentence)  # Print the server's response

clientSocket.close()  # Close the client socket