---
title: Chris Dannen - Introducing Ethereum and Solidity: Foundations of Cryptocurrency and Blockchain Programming for Beginners - 2017
created: 2018-05-26
taxonomy:
  category: [Technology]
  status: draft
---

## Context

## Learned in this study

## Things to explore
* Having every transactions stored on every node of the network seems like a huge waste of space
* Is the cost of using the Ethereum network based on the number of instructions of your contract? In other words, how much CPU time you need to execute it
* How does the network decide which node will execute a smart contract?
	* How do you prevent duplicate execution?
	* Are all nodes supposed to execute the smart contract?
* The ability to have decade-old smart contracts still execute seems to rely on the programming language used to describe the smart contract... How can we guarantee said language will still exist in a few decades?
* Where is ether coming from?
* It seems wasteful to execute contracts which have too low transaction fee, but is it possible to determine a contract cost in order to avoid this execution?

# Overview
* Ethereum could be considered as an OSI layer (encapsulating higher levels)

# Notes
## Chapter 1 - Bridging the Blockchain Knowledge Gap
### What Ethereum Does
* In Ethereum, smart contracts are written in the programming language Solidity

### Three Parts of a Blockchain
* A blockchain can be thought of as a database that is distributed, or duplicated, across many computers
* The innovation represented by the word blockchain is the specific ability of this network database to reconcile the order of transactions, even when a few nodes on the network receive transactions in various order
* What is widely called a blockchain is really the combination of three technologies
	* Peer-to-peer networking
	* Asymmetric cryptography: In Bitcoin and Ethereum, asymmetric cryptography is used to create a set of credentials for your account, to ensure that only you can transfer your tokens
	* Cryptographic hashing
* Adam Back released Hashcash in 2002, which pioneered the use of mining to send transactions
* Satoshi Nakamoto added distributed consensus to this innovation with the creation of Bitcoin in 2009

#### Ethereum Assumes Many Chains
* Ethereum was built with the assumption that copycats are a foregone conclusion, and that there may be many blockchains, and thus there should be a set of protocols in place by which they can communicate

### Ether as a Currency and Commodity
#### Gresham's Law
* In an economy, "bad" money drives out "good." In other words, people save and hoard currencies they expect to appreciate in value, while spending currencies they expect to depreciate in value

#### The Path to Better Money
* Ether can be used to pay to run programs on Ethereum's network
* Ether can be considered a commodity

#### Cryptoeconomics and Security
* What makes systems like Ethereum and Bitcoin so secure is that they are not based on any hack-proof technology but rather rely on powerful financial incentives and disincentives to keep malefactors at bay

#### Back to the Good Old Days
* The Ethereum network functions as one large computer which executes programs in lockstep; it is a machine which is "virtualized" by a network of other machines

### What Smart Contracts (Really) Do
* Smart contract: some business logic that runs on the network, semi-autonomously moving value and enforcing payment agreements between parties

### Where's the Data
* How transactions are recorded in Ethereum: it's all stored on every node of the network

### Deciding Where You Fit In
* The Ethereum network is a fully redundant distributed database, with copies on every node. That means you can trust your application to fire off a call when a certain condition is met, even if that condition happens decades into the future - and even if the nodes have all changed

### What You Can Build Today
#### The Promise of Decentralized Databases
* Like all databases, a blockchain has a schema: rules define, constrain, and enforce relationships between entities
* In all databases, shared read/write access creates enormous complexity

## Chapter 2 - The Mist Browser
* Two types of client applications: wallets and full nodes
	* Wallet: A lightweight node that connects to a blockchain to perform basic functions, such as sending and receiving cryptocurrency
	* Full node: Command-line interface that can perform the full gamut of operations allowed by the network

### Wallets as a Computing Metaphor
#### Your Address is What?
* An account is a data object: an entry in the blockchain ledger, indexed by its address, containing data about the state of that account, such as its balance
* An address is a public key belonging to a particular user

### Breaking with Banking History
* No individual has the power to create more ether

### Working with Messages and Transactions
* Transactions are used to refer to state changes in the distributed database
* Messages are data objects passed back and forth across the network between smart contracts, and do not necessarily result in any changes being made on the chain

### Transactions Change State
* A transaction in Ethereum refers to a piece of data bearing a cryptographic signature, which goes in the blockchain, and is thus recorded on every node in the network
* Every transaction triggers a message to accomplish this state change, but messages are also sent by EVM code

### So, What Is a Blockchain?
* A block is a unit of time that encompasses a certain number of transactions

### Paying for Transactions
* The EVM requires a tiny fee to process the transaction
* By forcing users to pay for transactions on the EVM, the likelihood of wasteful never-ending programs being executed is theoretically reduced
* These costs are priced in a unit called gas
	* You can think of gas as a metric indicating the number of steps the EVM will have to take to complete the instructions in the transaction
* Whether or not a transaction executes is determined by the amount of gas the sender is willing to pay. If the total number of steps exceeds the gas budgeted for a transaction, all steps are rolled back, and no part of the transaction is executed. If a user sends a transaction with too low a transaction fee, it will be processed only after some time, or not at all

## Chapter 3 - The EVM
* The EVM is a single, global 256-bit "computer" in which all transactions are local on each node of the network, and executed in relative synchrony

### What are Virtual Machines, Exactly?
* A virtual machine is an emulation of a computer system by another computer system

### What the EVM Does
* The EVM can run arbitrary computer programs written in the Solidity language

### Blocks The History of State Changes
* Transactions and state changes in the Ethereum network are segmented into blocks, and then hashed
* Each block is verified and validated before the next canonical block can be placed on "top" of it

#### Understanding Block Time
* In Bitcoin, a block is 10 minutes
* In Ethereum, block time is not a function of the issuance schedule of ether. Instead, block time is a variable that is kept as low as possible, for the sake of speedy transaction confirmation

### Renting Time on the EVM
* For every instruction the EVM executes, there must be a cost associated, to ensure the system isn't jammed up by useless spam contracts

#### Why Is Gas So Important?
* Gas cost ensure that computation time on the network is appropriately priced
* Fees in the EVM are based on the amount of work being done, not on the size of the transaction

### Working with Gas
#### How Gas Relates to Scaling the System
* There is no way to jam up the EVM without paying a lot, in the form of transactions fees, to do it
* Scaling is handled in a de facto way through the gas fee system
* Miners are free to choose the transactions that pay the highest fee rates, and can also choose the block gas limit collectively
* The gas limit determines how much computation can happen (and how much storage can be allocated) per block

### Accounts, Transactions, and Messages
#### Externally Owned Accounts
* Contains a balance of ether
* Capable of sending transactions
* Controlled by the account's private keys
* Has no code associated with it
* A key/value database contained in each account, where keys and values are both 32-byte strings

#### Contract Accounts
* Have an ether balance
* Hold some contract code in memory
* Can be triggered by humans (sending a transaction) or other contracts sending a message
* When executed, can perform complex operations
* Have their own persistent state and can call other contracts
* Have no owner after being released to the EVM
* A key/value database contained in each account, where keys and avlues are both 32-byte strings

### Transactions and Messages
#### Characteristics of Transactions
* A recipient address; specifying no recipient is the method for uploading new smart contracts
* A signature identifying the sender
* A value field showing the amount being sent
	* An optional data field, for a message (if this is being sent to a contract address)
* A STARTGAS value
* A GASPRICE value

#### Characteristics of Messages
* A chunk of data sent by a contract to another contract (never to or from a human)
* Messages are virtual objects that are never serialized and exist only in the EVM

# See also

# References
