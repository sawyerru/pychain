'''
BlockClass.py - Block object and supporting functions for each block object 
within a blockchain
'''
from datetime import datetime  
import hashlib  
import random
import time
  
  
class Block(object):  
    '''
    Block Object to contain block information:
        Transactions, 
        Merkle Root,
        Timestamps,
        Index, 
        Previous Hash, 
        Hash
    '''
      
    def __init__(self, index=None, previous_hash=None, merkle_root=''):    
        # Contains all instance attributes
        
        # Public member variables
        self.index = index  
        self.previous_hash = previous_hash  
        self.merkle_root = merkle_root  
        self.timestamp = datetime.now()
        self.hash = None
        
        # Protected member variables (only for use inside class and inherited classes)
        self._next_block = None # used to iterate through data structure 
        self._block_size = 10 
        self._transactions = []
        
    def mine(self):
        ''' Mine the block given the current data. Use Proof function and hash block data to finalize block
        '''
        # Raise error if some information is missing
        if self.index is None or self.previous_hash is None or self.merkle_root == '':
            raise Exception('Cannot mine - block header information not complete')
        
        # Do Proof
        if self.do_proof():    
            # Finalize hash
            self.hash = self.calc_hash(self.index, self.timestamp, self.previous_hash, self.merkle_root)
            return 'Block {} Mined! New Hash = {}'.format(self.index, self.hash)
        else:
            raise Exception('Cannot mine - proof not found')
    
    @staticmethod
    def do_proof():
        attempts = 0
        p = int(random.random() * 100) # random.random() returns a number between 0.0 and 1.0 -> we want to make it an int in the 100s
        a = random.randint(2, p-1)
        
        # use fermat's little theroem to determine if p is prime
        while (a**p) % p != a % p and attempts >= 10: # p is not prime, try again
            print('MINING ATTEMPT: ', attempts, end='', flush=True)
            p = int(random.random() * 100) # random.random() returns a number between 0.0 and 1.0 -> we want to make it an int in the 100s
            a = random.randint(2, p-1)
            attempts += 1
            time.sleep(1)
        
        return True if attempts < 10 else False # no prime number found in max attempts
        
    @staticmethod # 'static method' decorator describes a function that does not use or change any member variables
    def calc_hash(index, timestamp, prev_hash, merkle_root):
        block_string = "{}{}{}{}".format(index,  timestamp, prev_hash, merkle_root )  
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def add_transaction(self, transaction):
        ''' Add Transaction to block
            transaction: dictionary Object of transaction
        '''
        if self._block_size == 0:
            raise Exception('Block {} Full - please mine me.'.format(self.index))
        transaction_string = str(transaction)
        self._transactions.append(transaction_string)
        self.merkle_root = hashlib.sha256(self.merkle_root.encode() + transaction_string.encode()).hexdigest()
        self._block_size -= 1
    
    
    def __repr__(self):
        ''' function gets called when print(Block()). Called the representation function. Do NOT change!'''
        width = 120
        str1 = "|" + "-"*width + "|"
        
        str2_blank = width - ((len(self.hash) if self.hash is not None else 4) + len(str(self.index)) + 7 + 8)
        str2 = '| Hash: {h:}'.format(h=self.hash) + ' '*str2_blank + 'Index: {i:} |'.format(i=self.index)

        str3_blank = width - ((len(str(self.previous_hash)) if self.previous_hash is not None else 4) +  len(str(self.timestamp)) + 13 + 12) 
        str3 = '| Prev. Hash: {ph:}'.format(ph=self.previous_hash) + ' '*str3_blank + 'Timestamp: {t:} |'.format(t=self.timestamp)
        
        str4_blank = width - (len(str(self.merkle_root)) + len(str(self._block_size)) + 14 + 13)
        str4 = '| Merkle Root: {mr:}'.format(mr=self.merkle_root) + ' '*str4_blank + 'Rem. Space: {s:} |'.format(s=self._block_size)
        
        str5 = "|" + "-"*width + "|"
        
        S = str1 + '\n' + str2 + '\n' + str3 + '\n' + str4 + '\n'
        
        for t in self._transactions:
            blanks = width - (len(t) + 7)
            s = "| ----> {}".format(t) + ' '*blanks +'|\n'
            S += s
        return S + str5

    def display(self):
        ''' Special Printing function to utilize __repr__. Do NOT Change.'''
        print(self)