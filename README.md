# hw19-Blockchain-Python


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