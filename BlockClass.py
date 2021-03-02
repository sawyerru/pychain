'''
BlockClass.py - Block object and supporting functions for each block object 
within a blockchain
'''
from datetime import datetime  
import hashlib  
  
  
class Block(object):  
      
    def __init__(self, index=None, previous_hash=None, merkle_root=''):    
        self.index = index  
        # self.proof = proof
        self.previous_hash = previous_hash  
        self.merkle_root = merkle_root  
        self.timestamp = datetime.now()
        self.hash = None
        
        self._next_block = None
        self._block_size = 10
        
    def mine(self):
        # do proof/consensus mechanism here and apply final block hash
        if self.index is None or self.previous_hash is None or self.merkle_root is '':
            raise Exception('Cannot mine - block header information not complete')
        
        # Do Proof
        
        
        # Finalize hash
        block_string = "{}{}{}{}".format(self.index,  self.timestamp, self.previous_hash, self.merkle_root )  
        self.hash = hashlib.sha256(block_string.encode()).hexdigest()
        return 'Block {} Mined! New Hash = {}'.format(self.index, self.hash)
        
    @staticmethod  # 'staticmethod' decorator means this funtion doesn't change the object
    def create_proof(previous_proof):  
        pass

    def add_transaction(self, transaction):
        if self._block_size == 0:
            raise Exception('Block {} Full - please mine me.'.format(self.index))
        transaction_string = str(transaction)
        self.merkle_root = hashlib.sha256(self.merkle_root.encode() + transaction_string.encode()).hexdigest()
        self._block_size -= 1
    
    
    def __repr__(self):
        width = 120
        str1 = "|" + "-"*width + "|"
        
        str2_blank = width - ((len(self.hash) if self.hash is not None else 4) + len(str(self.index)) + 7 + 8)
        str2 = '| Hash: {h:}'.format(h=self.hash) + ' '*str2_blank + 'Index: {i:} |'.format(i=self.index)

        str3_blank = width - ((len(str(self.previous_hash)) if self.previous_hash is not None else 4) +  len(str(self.timestamp)) + 13 + 12) 
        str3 = '| Prev. Hash: {ph:}'.format(ph=self.previous_hash) + ' '*str3_blank + 'Timestamp: {t:} |'.format(t=self.timestamp)
        
        str4_blank = width - (len(str(self.merkle_root)) + len(str(self._block_size)) + 15 + 13)
        str4 = '| Transactions: {mr:}'.format(mr=self.merkle_root) + ' '*str4_blank + 'Rem. Space: {s:} |'.format(s=self._block_size)
        
        str5 = "|" + "-"*width + "|"
        
        return str1 + '\n' + str2 + '\n' + str3 + '\n' + str4 + '\n' + str5

    def display(self):
        print(self)