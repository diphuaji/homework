from socket import *
import time
serverName = '192.168.0.15'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
message='lower case'
result=[[0 for i in xrange(25)] for i in xrange(5)]
for m in xrange(5):
	print 'm=%s for this round' % (m+1,)
    clientSocket.settimeout(m+1)
    for n in xrange(25):
        valid_count=0
        for i in xrange(n+1):
            try:
                start_time=time.time()
                print 'clientPing_v1 %s %s %s'  % (n+1,i+1,start_time)
                clientSocket.sendto(message.encode(), (serverName, serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                end_time=time.time()
                delta=end_time-start_time
                result[m][n]+=delta
                valid_count+=1
                print "message from server: " + modifiedMessage.decode()
                print "RTT: %f" % (delta,)
            except timeout as e:
                print 'Request time out'
        if valid_count:
            result[m][n]/=valid_count
for r in result:
    print r
clientSocket.close()


