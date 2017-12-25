#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
print('socket successfully created')
#Prepare a sever socket
#Fill in start
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
#Fill in end
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send('\nHttp/1.1 200 OK\n\n'.encode())
        #Fill in end
        connectionSocket.send(outputdata.encode())
        #Send the content of the requested file to the client
        #for i in range(0, len(outputdata)):
        #    connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        #Fill in start
        connectionSocket.send('\nHttp/1.1 404 Not Found\n\n'.encode())
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
serverSocket.close()