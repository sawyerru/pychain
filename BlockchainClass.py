'''
BlockchainClass.py - Blockchain class and supporting functions. 
'''

from BlockClass import Block

class Blockchain(object):  
      
    def __init__(self):  
        # Member Variables (attributes about the blockchain object that may be useful)
        self.genesis_block = None
        self.current_length = 0
        self._create_genesis_block()  
      
    def _create_genesis_block(self):
        ''' The genesis block is a special block that has no previous hash and 
        serves as the foundation of the entire blockchain. We create it right 
        when the blockchain itself is created.'''
        self.genesis_block = Block(index=len(self.chain), proof=0, previous_hash=0)

     
    @property  
    def get_last_block(self):
        block = self.genesis_block
        while block.next_block is not None:
            block = block.next_block
        return block