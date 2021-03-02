from BlockchainClass import Blockchain
from BlockClass import Block

import hashlib  


def create_transaction():
    transaction_object = {'to': None, 'from': None, 'amt': None}
    transaction_object['to'] = input('To? ').strip()
    transaction_object['from'] = input('From? ').strip()
    transaction_object['amt'] = input('Amount? ').strip()
    
    return transaction_object


def main():
    print('*******************************')
    print('  *Entering the Blockchain     ')
    print('*******************************')
    
    blockchain = Blockchain()
    
    # State information is outside user interface loop
    current_block = Block(index=blockchain.current_length+1, previous_hash=blockchain.genesis_block.hash)
    prev_block = blockchain.get_last_block()

    # User interface loop operates until they're finished
    while True:
      
        print('\n\nMENU:---------------------------------')
        print("\t '.' - exit the program")
        print("\t 'T/t' - Create a new transaction")
        print("\t 'mine' - mine the current block")
        print("\t 'chain' - display the entire chain")
        print("\t 'block' - display the current block")
        print("\t 'V/v' - check blockchain is valid")
        print('--------------------------------------')
        option = input('Please select a menu option: ').strip().lower()
        
        if option == '.':
            print('*Exiting the Blockchain*')
            break
        elif option == 't': 
            transaction_object = create_transaction()
            try: 
                current_block.add_transaction(transaction_object)   
            except Exception as err:
                print(err)
        
        elif option == 'mine':
            # Mine current block and add to ledger
            try:
                result = current_block.mine()
                print(result)
               
                blockchain.append_block(current_block)
            
                # adjust pointers and state of chain
                prev_block._next_block = current_block
                prev_block = current_block
                current_block = Block(index=blockchain.current_length + 1, previous_hash=prev_block.hash)
            except Exception as err:
                print(err)
            
            
        elif option == 'chain':
            blockchain.display()
        elif option == 'block':
            current_block.display()
            
        elif option == 'v':
            result = blockchain.check_validity()
            print(result)
            
        else:
            print('Invalid Argument: ', option, '\n please try again')
        
if __name__ == "__main__":
    main()