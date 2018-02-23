from socket import *
serverName = 'localhost'
#serverName = '142.132.141.241'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From server: ', modifiedSentence.decode())

clientSocket.close()


