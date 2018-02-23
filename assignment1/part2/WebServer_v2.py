#import socket module
from socket import *
from threading import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
port=12209
serverSocket.bind(('', port))
serverSocket.listen(1)
#Fill in end

#BOF function to process a request
def do_request(connectionSocket,addr):
    try:
        message = connectionSocket.recv(1024).decode()#Fill in start #Fill in end
        filename=message.split()[1]
        f=open(filename[1:])
        outputdata=f.readlines()#Fill in start #Fill in end
        runtime_filename='HelloWorldPort_%s.html' % (addr[1],)
        runtime_file=open(runtime_filename,'w')        
        for i in range(0, len(outputdata)):
            runtime_file.write(outputdata[i])
        f.close()
        runtime_content="<p><b>YOUR IP IS: %s</b></p><p><b>THE PORT USED BY YOUR BROWSER IS: %s</b></p>" % (addr[0],addr[1])        
        runtime_file.write(runtime_content);
        runtime_file.close();
        #open the newly created file
        f=open(runtime_filename)
        outputdata=f.readlines()
        f.close()
        length=0
        for i in range(0, len(outputdata)):
            length+=len(outputdata[i])    
        #Send one HTTP header line into socket
        #Fill in start
        header="HTTP/1.1 200 OK\r\n"+\
            "Content-Type: text/html; charset=utf-8\r\n"+\
            "Content-Length: %d\r\n\r\n"
        connectionSocket.send(header % (length))
        #Fill in end
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])

        connectionSocket.send("\r\n")
        connectionSocket.close()
    except IOError:        
        #Send response message for file not found
        #Fill in start
        body="HTTP/1.1 404 Not Found\r\n"+\
            "Content-Type: text/plain; charset=utf-8\r\n"+\
            "Content-Length: %d\r\n\r\n%s"
        outputdata="404 Not Found."
        connectionSocket.send(body % (len(outputdata),outputdata))
        #Fill in end
        #Close client socket
        #Fill in start
        connectionSocket.close()
        #Fill in end
#EOF function to process a request

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()
    t=Thread(target=do_request,args=(connectionSocket,addr))
    t.start()
serverSocket.close()
