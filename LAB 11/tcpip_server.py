from socket import*
serverPort=12000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(("127.0.0.1",serverPort))
print("the server is ready to recieve")
while 1:
    sentence,clientAddress=serverSocketrecvfrom(2048)
    sentence=sentence.decode("utf-8")
    file=open(sentence,"r")
    l=file.read(2048)

    serverSocket.sendto(bytes(1,"utf-8"),clientAddress)

    print("\nSent contents of",end)
    print(sentence)
    #for i in sentence:
      #printI=(str(i),end=")
    file.close()
