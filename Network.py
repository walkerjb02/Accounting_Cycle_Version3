from Financial_Accounting import *
import socket
import time
import threading as tr
from Blockchain import C
from Hashbank import Bank

class server:
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serverSocket.bind(('', 0))
        self.serverIP = '10.0.0.46'
        self.serverPort = self.serverSocket.getsockname()[1]
        print("serverIP:\t" + self.serverIP)
        print("serverPort:\t" + str(self.serverPort))
        self.message = str(self.serverPort)
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientportmessage = []
        self.verification_hash = ['0']
        self.journal_data = ['0']
        self.timestamp = ['0']
        self.bank = ['0']

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
                self.messagesend()
                n += 1
                time.sleep(5)
            else:
                pass

    def messagesend(self):
        message = v.addblock()
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
                hashid = '0x'
                if hashid in str(self.inbound):
                    self.inbound = str(self.inbound)
                    self.verification_hash = [''.join(c for c in self.inbound[0:self.inbound.index('>'):])]
                    self.journal_data = [''.join(d for d in self.inbound[self.inbound.index('>'):self.inbound.index('<')])]
                    self.timestamp = [''.join(e for e in self.inbound[self.inbound.index('<'):self.inbound.index('*'):])]
                    self.bank = [''.join(f for f in self.inbound[self.inbound.index('*') + 1:-1:])]
                    if self.verification_hash not in Bank[-1]:
                        self.verifyexternal()
                else:
                    itera = 'aeiouy'
                    for a in itera:
                        if a in str(self.inbound):
                            self.inbound = str(self.inbound)
                            if self.inbound != dupprotect[-1]:
                                dupprotect.append(self.inbound)
                                print(str(self.inbound))



    def verifyexternal(self):
        new = C.mine(Bank[-1], self.journal_data, self.timestamp)
        if new == self.verification_hash:
            C.add_to_chain()
            dbr = [a for a in self.journal_data[self.journal_data.index('>') + 1:self.journal_data.index('%'):]]
            cbr = [b for b in self.journal_data[self.journal_data.index('%') + 1:self.journal_data.index('#'):]]
            dje = [c for c in self.journal_data[self.journal_data.index('#') + 1:self.journal_data.index('@'):]]
            ret_earn = [d for d in self.journal_data[self.journal_data.index('@') + 1:self.journal_data.index('!'):]]
            ni = [e for e in self.journal_data[self.journal_data.index('!') + 1:self.journal_data.index('<'):]]
            with open('Storage_Current.py', 'w') as storage:
                storage.write(f'dbr = {dbr}\ncbr = {cbr}\ndje = {dje}\nret_earn = {ret_earn}\nni = {ni}\n')
                storage.close()
            with open('Storage_Journal.py', 'a') as jstorage:
                jstorage.write(f'\n{self.verification_hash}\n')
                jstorage.write(f'dbr = {dbr}\ncbr = {cbr}\ndje = {dje}\nret_earn = {ret_earn}\nni = {ni}\n')
                jstorage.close()
            with open('Hashbank.py', 'w') as B:
                B.write(f'Bank = [{self.bank}]')
            print('External Change Verified!')
        elif new != self.verification_hash:
            print('External Change Not Verified!')


s = server()


