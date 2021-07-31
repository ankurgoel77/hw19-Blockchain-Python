# hw19-Blockchain-Python

## Generate a Mnemonic

Running the following command:

> ./derive --gen-key -g --outfile=keys

generates a file called keys with 3 different keys off the same mnemonic in BTC.  That mnemonic is as follows and is stored in .env :

> beyond subway club silk jeans art cargo burger royal mass conduct lava danger broken copy luxury adult eyebrow pond friend crowd blade flower menu

## BTC Testnet

_See tbtc.ipynb for the code below:_

From the Mnemonic above, we can use the "coins" dictionary from derive_wallet to get some addresses:
> address : n2otMud2rjqdxhcg7M1MTxpoaC7nfsHFd2  
> address : mw1cuQdMZSnaZgUgQwNEAsLDyzCyG31gs8  
> address : mwCvjNk53q27NsKWfDnn7rQpVa1yhakxp6  
> original faucet address : mkHS9ne12qx9pS9VojpwU5xtRd4T7X7ZUt  

With the first address, I was able to fund with it with 0.001 tBTC using this faucet at https://testnet-faucet.mempool.co/

I confirmed the transaction on the Testnet Explorer at https://tbtc.bitaps.com/n2otMud2rjqdxhcg7M1MTxpoaC7nfsHFd2 where you can see the initial funding with Transaction ID d367504fffe55a24b1d792c361b712d0c704268200148714203b5f20520e82c1

Once I funded my initial address, it was time to use wallet.py to transfer that to a 2nd address.  Initially I tried to transfer the entire 0.001 tBTC, but that failed due to fees, so I ended up transferring only 0.0005 tBTC.  Please see tx.ipynb for the following code:

> from wallet import *  
> address1 = coins[BTCTEST][0]["address"]  
> privkey = coins[BTCTEST][0]["privkey"]  
> acct1 = priv_key_to_account(BTCTEST, privkey)  
> recipient = coins[BTCTEST][1]["address"]  
> tx = send_tx(BTCTEST, acct1, recipient, 0.00005)

This resulted in a transaction with id 8a61e9dc06ced7553e3a5d5ec3ee507036104866a67c838e789641277917bd8f.  The resulting transcation is confirmed at https://tbtc.bitaps.com/mw1cuQdMZSnaZgUgQwNEAsLDyzCyG31gs8 with the following screenshot:

![btctestnet confirmed](screenshots/btc_testnet_confirmed.png)

The transaction itself shows how the tBTC flowed from address1 to address2 as follows:

![btctestnet tx](screenshots/tbtc_tx.png)

## Proof of Work blockchain
I used geth and puppeth to create a proof of work blockchain with the following commands:

> ../blockchain-tools/geth account new --datadir node1  
> ../blockchain-tools/geth account new --datadir node2  

No passwords are setup for the keystore files on these nodes.  The addresses are:  
Node 1 : 0xd9e6c0546cd406a40a2e96cf0b433f13816d6626  
Node 2 : 0xc5e9d741256f3b093fd33eb2ffe5e4384b83f2f8

> ../blockchain-tools/puppeth  

Note that with puppeth, I chose to make a Proof-Work, a network name of hw18_pow, and with a chain ID of 4668. I also pre-funded the address of both nodes.

> ../blockchain-tools/geth init hw19_pow.json --datadir node1  
> ../blockchain-tools/geth init hw19_pow.json --datadir node2

> ../blockchain-tools/geth --datadir node1 --mine --miner.threads 1   
> ../blockchain-tools/geth --datadir node2 --port 30304 --rpc --ipcdisable --bootnodes "enode://d18c6562c6717149ac3f2a3994c1e1c7fd7c5a493f87533bcee0e30e0655ecbeb6129f37f536059342e112fe084f9c4cb206ca1cd144e51bcdd53c6d1f98053f@127.0.0.1:30303"

As a test, I sent a 1 ETH transaction in MyCrypto between these 2 addresses as shown in the MyCrypto screenshot below:
![transaction completed](screenshots/tx_confirmed.png)

Once the blockchain was active, I ran the following code in eth.ipynb to transfer 250 ETH from the address of Node1 to the address of Node2:

> from wallet import *  
> address1 = "0xd9e6c0546cd406a40a2e96cf0b433f13816d6626"  
> privkey = "0x499599facc2d9cbe7281f323cfa076bb45b99270d705e89befe4097a5fad5651"  
> acct1 = priv_key_to_account(ETH, privkey)  
> recipient = Web3.toChecksumAddress("0xc5e9d741256f3b093fd33eb2ffe5e4384b83f2f8")  
> tx = send_tx(ETH, acct1, recipient, int(250e18))  
> print(tx.hex())  

This resulted in a transaction ID of 0x344b14b1c985557e2fe403217a45569aecbbb243477a5a25cbddd84e37c63f6a

MyCrypto was able to confirm this transaction on my blockchain:

![eth tx confirmed](screenshots/eth_tx_confirmed.png)