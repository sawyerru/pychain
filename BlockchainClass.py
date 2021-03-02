''' BlockchainClass.py - Blockchain class and supporting functions.

In this implementation we are avoiding using a list to hold block objects. This 
decision is to help work on data structures more complex than lists and give a 
better idea of how blockchains link data together. (Hint: if you're stuck, try 
looking up Linked Lists and do some reading.) 
'''

from BlockClass import Block

class Blockchain(object):  
      
    def __init__(self):  
        # Member Variables (attributes about the blockchain object that may be useful)
        self.genesis_block = self._create_genesis_block()
        self.current_length = 0
        self.nonce = 0        
         
      
    def _create_genesis_block(self):
        ''' The genesis block is a special block that has no previous hash and 
        serves as the foundation of the entire blockchain. We create it right 
        when the blockchain itself is created.'''
        genesis_block = Block(index=0, previous_hash=0, merkle_root=0)
        genesis_block.mine()
        return genesis_block

    def append_block(self, block):
        ''' Since a blockchain is an append-only ledger we will only be adding 
        new blocks to the last block in thee chain'''
        self.get_last_block()._next_block = block
        self.current_length += 1
        
    def check_validity(self):
        block = self.genesis_block
        while block._next_block is not None:
            if block._next_block.previous_hash != block.hash:
                return False
            block= block._next_block
        return True
     
    def get_last_block(self):
        block = self.genesis_block
        while block._next_block is not None:
            block = block._next_block
        return block
    
    def display(self):
        width = 120
        block = self.genesis_block
        while block is not None:
            block.display()
            print(' '*int(width/2 - 1) + '0' + ' '*int(width/2 - 1))
            print(' '*int(width/2 - 2) + '( )' + ' '*int(width/2 - 2))
            print(' '*int(width/2 - 1) + '0' + ' '*int(width/2 - 1))
            block = block._next_block
        