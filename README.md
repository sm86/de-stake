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
| Aptos           | Joelton      | [white paper](https://aptos.dev/aptos-white-paper/) | 
| Axelar | Tendermint | [docs](https://github.com/axelarnetwork/axelar-core/blob/main/docs/cli/axelard_tendermint_version.md)|
| BNB (Binance) | Tendermint|[white paper](https://github.com/bnb-chain/whitepaper/blob/master/WHITEPAPER.md)|
| Celestia | Tendermint | [docs](https://docs.celestia.org/learn/how-celestia-works/data-availability-layer)|
| Celo | IstanbulBFT | [docs](https://docs.celo.org/protocol/consensus) |
| Cosmos | Tendermint | [blog](https://blog.cosmos.network/tendermint-explained-bringing-bft-based-pos-to-the-public-blockchain-domain-f22e274a0fdb) |
| Injective | Tendermint | [blog](https://medium.com/@charlesace/injective-tendermint-core-a-powerful-consensus-engine-for-decentralized-finance-a1db298b0b70)|
| Osmosis | Tendermint | [docs](https://docs.osmosis.zone/overview/educate/terminology#consensus) |
| Polygon | Tendermint | [docs](https://wiki.polygon.technology/docs/pos/design/heimdall/peppermint/)|
| Sui | Mysticeti                   | [docs](https://docs.sui.io/guides/operator/validator-committee) |



For each blockchain, we save stake distribution data in CSV format, with two columns: `address` and `tokens`.

The CSV file has following format DDMMYY_blockchain.csv and is stored in [data](data/) folder. 

# API Server
Added API for these metrics. Start the server:
```python3 api/app.py```
Access the data:
```http://127.0.0.1:5000/metrics/<date>```

The date has to be in right range, else you would get the following error:
``` 
{
  "error": "No data available for the selected date. Please select a date between 24-10-2023 and today"
}
```
