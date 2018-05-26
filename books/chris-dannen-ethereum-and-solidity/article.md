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

# See also

# References
