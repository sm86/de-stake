# DeStake: Decentralized Stake Distribution Insights
Analyzing stake among validators in PoS blockchains.

## Overview
This repository focuses on analyzing decentralization in Proof of Stake (PoS) blockchains by collecting and analyzing validator and staking data. 

## Instructions to Run
1. Clone the repository:
   
   ``` git clone https://github.com/sm86/decentralized_stake_insights.git ```
3. Run the main file:

   ``` cd decentralized_stake_insights && python3 data.py```
## Blockchains 
We only collect validator stake data on blockchains leveraging **classical BFT consensus mechanisms** and variants. 

In other words, blockchains that require a super majority quorum (two-thirds of total stake) on every block. Below are the list of blockchains


| Blockchain      | Consensus Mechanism                | Reference |
|-----------------|------------------------------------|-----------|
| Aptos           | DiemBFT (HotStuff)       | [white paper](https://aptos.dev/aptos-white-paper/) | 
| Axelar | Tendermint | [docs](https://docs.axelar.dev/validator/operations/monitoring)|
| BNB (Binance) | Tendermint|[white paper](https://github.com/bnb-chain/whitepaper/blob/master/WHITEPAPER.md)|
| Cosmos | Tendermint | [blog](https://blog.cosmos.network/tendermint-explained-bringing-bft-based-pos-to-the-public-blockchain-domain-f22e274a0fdb) |
| Osmosis | Tendermint | [docs](https://docs.osmosis.zone/overview/terminology/#consensus) |
| Polygon | Tendermint | [docs](https://wiki.polygon.technology/docs/pos/design/heimdall/peppermint/)|
| Sui | Narwhal/BullShark                     | [docs](https://docs.sui.io/learn/architecture/consensus) |



For each blockchain, we save stake distribution data in CSV format, with two columns: `address` and `tokens`.

The CSV file has following format DDMMYY_<chain>.csv and is stored in [data](data/) folder. 
