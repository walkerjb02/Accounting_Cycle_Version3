from SHA256 import *
import os
from Hashbank import Bank

class blocks:
    def components(self, previoushash, data, date):
        return('{}{}{}'.format(previoushash, data, date))

b = blocks()

class Chain:
    def mine(self,previous, data, date):
        self.Bank = Bank
        next = ma.hash(b.components(previous, data, date))
        self.Bank.append(next)

    def add_to_chain(self):
        self.Bank = list(set(self.Bank))
        with open('Hashbank.py', "w") as bank:
            bank.write(f'Bank = {self.Bank}')
        bank.close()

C = Chain()

