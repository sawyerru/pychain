'''
BlockClass.py - Block object and supporting functions for each block object 
within a blockchain
'''
import time  
import hashlib  
  
  
class Block(object):  
      
    def __init__(self, index=None, previous_hash=None, merkle_root=''):    
        self.index = index  
        # self.proof = proof
        self.previous_hash = previous_hash  
        self.merkle_root = merkle_root  
        self.timestamp = time.time()
        self.hash = None
        
        self._next_block = None
        self._block_size = 10
        
    def mine(self):
        # do proof/consensus mechanism here and apply final block hash
        if self.index is None or self.previous_hash is None or self.merkle_root is None:
            return 'Cannot mine - block header information not complete'
        
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
            return 'Block {} Full - please mine me.'.format(self.index)
        transaction_string = str(transaction)
        self.merkle_root = hashlib.sha256(self.merkle_root.encode() + transaction_string.encode()).hexdigest()
        self._block_size -= 1
        
        
        
    # @property  # 'property' decorator means that it doesn't change the object - (often used for setter and getter functions)
    # def calculateHash(self):  
    #     block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)  
    #     return hashlib.sha256(block_string.encode()).hexdigest()
    
    def __repr__(self):
        return '|-|\n|Hash: {h:}\tIndex: {i:}|\n|Prev. Hash: {ph:}\tTimestamp: {t:}|\n|Transactions: {mr:}\tSpace Remaining: {s:}||--|'.format(h=self.hash, i=self.index, ph=self.previous_hash, t=self.timestamp, mr=self.merkle_root, s=self._block_size )

    def display(self):
        print(self)