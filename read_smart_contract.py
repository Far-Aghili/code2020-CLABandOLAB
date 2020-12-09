import json
from web3 import Web3

# Set up web3 connection with Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

#Choose the tag (IoT device that you want to authenticate)
ID=0# Based on Identity of the tag
web3.eth.defaultAccount = web3.eth.accounts[ID]

# Greeter contract ABI # based on your samart contract
abi = json.loads('[{"inputs": [],"name": "Greeter","outputs": [],"stateMutability": "nonpayable","type": "function"},{"inputs": [],"name": "greet","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [],"name": "greeting","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "string","name": "_greeting","type": "string"}],"name": "setGreeting","outputs": [],"stateMutability": "nonpayable","type": "function"}]')

# Greeter contract address - convert to checksum address
address = web3.toChecksumAddress('0x492EC9c3cB5358A9969f520b2D1b97f0824AC82B') # based on your address

# Read the default greeting and print it
contract = web3.eth.contract(address=address, abi=abi)
print(contract.functions.greet().call())
