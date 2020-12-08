import json
from web3 import Web3
import hashlib

HashOLABorCLAB=hashlib.sha256(b"PID_T\|PID_R\|X").hexdigest()

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
ID=0# Based on Identity of the tag
# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org

# Set a default account to sign transactions - this account is unlocked with Ganache
web3.eth.defaultAccount = web3.eth.accounts[ID]
# Greeter contract ABI # based on your smart contract
abi = json.loads('[{"inputs": [],"name": "Greeter","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "greet","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"}]')
# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('0x492EC9c3cB5358A9969f520b2D1b97f0824AC82B') # based on your address
# Initialize contract
contract = web3.eth.contract(address=address, abi=abi)
# Set a new greeting
tx_hash = contract.functions.setGreeting('New Id2').transact()
# Wait for transaction to be mined
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(
    contract.functions.greet().call()
))
