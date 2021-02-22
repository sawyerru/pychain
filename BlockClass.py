'''
BlockClass.py - Block object and supporting functions for each block object 
within a blockchain
'''
import time  
import hashlib  
  
  
class Block(object):  
      
    def __init__(self, index, proof, previous_hash, merkle_root):          
        self.index = index  
        self.proof = proof
        self.previous_hash = previous_hash  
        self.merkle_root = transactions  
        self.timestamp = time.time()
        
    
    @staticmethod  # 'staticmethod' decorator means this funtion doesn't change the object
    def create_proof_of_work(previous_proof):  
        """  
        Generate "Proof Of Work"  
        A very simple \`Proof of Work\` Algorithm -  
        -> Find a number such that, Sum of the number and previous POW number is divisible by 7  
        """  
        proof = previous_proof + 1  
        while (proof + previous_proof) % 7 != 0:  
            proof += 1  
      
        return proof  
    
    @property  # 'property' decorator means that it doesn't change the object - (often used for setter and getter functions)
    def get_block_info(self):  
        block_string = "{}{}{}{}{}".format(self.index, self.proof, self.previous_hash, self.transactions, self.timestamp)  
        return hashlib.sha256(block_string.encode()).hexdigest()
