# Import dependencies
import subprocess
import json
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
 
 
# Create a function called `derive_wallets`
""" 
derive_wallets

This function takes 4 inputs
    mnemonic : str
        A set of words that makes a valid mnemonic
    coin: str
        A shorthand for the kind of coin to derive keys for
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
coins["eth"] = derive_wallets(mnemonic, "eth", 3, "json")
coins["btc-test"] = derive_wallets(mnemonic, "btc-test", 3, "json")
pprint(coins)
print(coins["eth"][0]['privkey'])

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account():
    pass

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx():
    pass

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx():
    pass
