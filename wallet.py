# Import dependencies
import subprocess
import json
from bit.network.services import NetworkAPI
from bit.transaction import sign_tx
from dotenv import load_dotenv
import os
from pprint import pprint

# Load and set environment variables
'''Keys were generated using the following command
        ./derive --gen-key -g --outfile=keys
'''
load_dotenv()
mnemonic=os.getenv("mnemonic")


# Import constants.py and necessary functions from bit and web3
from constants import *
from web3 import Account, Web3
from bit import PrivateKeyTestnet

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
 
# Create a function called `derive_wallets`
""" 
derive_wallets - creates a dict full of wallet data

This function takes 4 inputs
    mnemonic : str
        A set of words that makes a valid mnemonic
    coin: str
        A coin from constants.py
    num_derive: int
        how many keys to generate
    format: str
        generally, format as json

"""
def derive_wallets(mnemonic, coin, num_derive, format):# YOUR CODE HERE):
    command = f'php ./derive -g --mnemonic="{mnemonic}"" --numderive={num_derive} --coin={coin} --cols=all --format={format}'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {}
coins[ETH] = derive_wallets(mnemonic, ETH, 3, "json")
coins[BTCTEST] = derive_wallets(mnemonic, BTCTEST, 3, "json")


# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
""" 
priv_key_to_account - converts a private key into an account based on coin type

This function takes 4 inputs
    coin: str
        A shorthand for the kind of coin to derive keys for
    priv_key: str
        a private key from a wallet

"""
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)
    else:
        return "error, unsupported coin"

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
""" 
create_tx - create the raw, unsigned transaction that contains all metadata needed to transact.

This function takes 4 inputs
    coin: str
        A coin from constants.py
    account: obj
        account object from priv_key_to_account
    to: str
        recipient address
    amount: int
        the amount of coin to send

"""
def create_tx(coin, account, to, amount):
    if coin == BTCTEST :
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    elif coin == ETH :
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": to, "value": amount}
        )
        return {
            "from": account.address,
            "to": to,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
            "chainId": 4668,
        }
    else:
        return "error, unsupported coin"

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
""" 
send_tx - call create_tx, sign the transaction, then send it to the designated network

This function takes 4 inputs
    coin: str
        A coin from constants.py
    account: obj
        account object from priv_key_to_account
    to: str
        recipient address
    amount: int
        the amount of coin to send

"""
def send_tx(coin, account, to, amount):
    if coin == BTCTEST :
        tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(signed_tx)
    elif coin == ETH :
        tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(tx)
        return w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    else:
        return "error, unsupported coin"

# address1 = coins[BTCTEST][0]["address"]
# privkey = coins[BTCTEST][0]["privkey"]
# print(f"The private key for the first address {address1} is: {privkey}")
# acct1 = priv_key_to_account(BTCTEST, privkey)
# print(acct1)
# recipient = coins[BTCTEST][1]["address"]
# tx = send_tx(BTCTEST, acct1, recipient, 0.0001)
# print(tx)