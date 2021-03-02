# Import some libraries needed for development
import time
import random

# Import BlockchainClass file and BlockClass file and import just the classes 
from BlockchainClass import Blockchain
from BlockClass import Block



def examples():
    # From BlockChainClass we create the BlockChain object
    blockchain = Blockchain() # This line will call the __init__ function from Blockchain class
    # now from the variable 'blockchain' we can access functions and member variables with '.'
    # like: blockchain.current_length
    
    block = Block(index=0, proof=0, previous_hash=0) # to make a block we need arguments (you can see these in the __init__)
    
    assert True # assert is a keyword used for testing conditions and states during runtime.
    
def test_blockchain_creation():
    blockchain = Blockchain()
    assert blockchain.genesis_block.hash is not None
    
    
    
    
    
if __name__ == '__main__':
    # Run all Test functions
    # examples()
    # test_blockchain_creation()
