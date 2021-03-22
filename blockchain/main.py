from blockchain import Blockchain

block_one_transactions = {"sender":"Selcuk", "receiver": "Ugur", "amount":"50"}
block_two_transactions = {"sender": "Ugur", "receiver":"Selcuk", "amount":"25"}
block_three_transactions = {"sender":"Ali", "receiver":"Ahmet", "amount":"35"}
fake_transactions = {"sender": "Murat", "receiver":"Mustafa, Ali", "amount":"100"}

local_blockchain = Blockchain()
#print(local_blockchain.print_blocks())
print(50*'*')
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)

print(local_blockchain.print_blocks())
local_blockchain.chain[2].transactions
local_blockchain.validate_chain()

