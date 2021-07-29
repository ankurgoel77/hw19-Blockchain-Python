# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os

# Load and set environment variables
'''Keys were generated using the following command
        ./derive --gen-key -g --outfile=keys
'''
load_dotenv()
mnemonic=os.getenv("mnemonic")
print(mnemonic)


# Import constants.py and necessary functions from bit and web3
from constants import *
 
 
# Create a function called `derive_wallets`
def derive_wallets():# YOUR CODE HERE):
    command = 1 # YOUR CODE HERE
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = 1# YOUR CODE HERE

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account():
    pass

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx():
    pass

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx():
    pass
