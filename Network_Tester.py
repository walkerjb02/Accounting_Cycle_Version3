import socket
import time
import threading as tr

class server:
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind(('', 0))
        self.serverIP = '10.0.0.46'
        self.serverPort = self.serverSocket.getsockname()[1]
        print(f"serverIP:{self.serverIP}")
        print(f"serverPort:{str(self.serverPort)}")
        self.clientportmessage = []
        self.message = str(self.serverPort)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connectionestablish(self):
        n = 0
        while 1:
            for i in range(0, int(self.serverPort)):
                self.clientSocket.sendto(self.message.encode(), (self.serverIP, i))
            for j in range(int(self.serverPort + 1), 65535):
                self.clientSocket.sendto(self.message.encode(), (self.serverIP, j))
            self.port, clientAddress = self.serverSocket.recvfrom(2048)
            if self.port:
                self.port = str(self.port.decode('UTF-8'))
                itera = '123456789'
                for a in itera:
                    if a in str(self.port) and len(self.port) == 5:
                        self.clientportmessage.append(self.port)
                    else:
                        pass
            self.clientportmessage = list(set(self.clientportmessage))
            if n < len(self.clientportmessage):
                print(f'Connection Established with {self.port}')
                n += 1
                time.sleep(5)
            else:
                pass

    def messagesend(self):
        while 1:
            message = input('Message?\n')
            n = 0
            while n < 2:
                for j in self.clientportmessage:
                    self.clientSocket.sendto(str(message).encode(), (self.serverIP, int(j)))
                n += 1


    def messagereceive(self):
        dupprotect = ['0']
        while 1:
            self.inbound, clientAddress = self.serverSocket.recvfrom(2048)
            if self.inbound:
                self.inbound = str(self.inbound.decode())
                itera = 'aeiouy'
                for a in itera:
                    if a in str(self.inbound):
                        self.inbound = str(self.inbound)
                        if self.inbound != dupprotect[-1]:
                            dupprotect.append(self.inbound)
                            print(str(self.inbound))
                        else:
                            pass


s = server()

tr.Thread(target=s.messagereceive).start()
tr.Thread(target=s.connectionestablish).start()
time.sleep(30)
tr.Thread(target=s.messagesend).start()


