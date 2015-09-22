# Multi-agent bot

## Learned in this study

## Things to explore

* Better input query format
* How dispatcher determines to which agent to dispatch a message
* What response format should be sent back to the dispatcher? To the user?
* What should the user receive as a response?

# Overview

The goal of this study is to look into the various ways to construct a network of bots that will interact with users.

The main goal is to attempt to create a framework on which developers may offer useful services to their users.

Similar to [IFTTT](https://ifttt.com/).

# Requirements

* Bots should be able to
	* communicate with one another
	* synchronize their data with one another (distributed database)
	* find one another (bot discovery/DHT)
* A user should be able to 
	* use a bot locally (without internet connection) and yet get useful results
	* send information to the bot
	* query the bot for information
	* interact with the bot through various ways (irc, email, slack, web, cli, etc.)
* Only authenticated users may use a bot

# Query processing

1. A user issues a query

	A query is minimally a string:
	
		my query
	
	However, a query can be very complex as well
	
		age =< 36
		name = Tom

2. An adapter (email, irc, shell, slack, web, etc.) takes the input query and converts it into a standardized format the dispatcher bot expects. The suggested format is similar to the command line arguments and options:

		my query --age =<36 --name =Tom
		weather --city=Montreal
		roll --min=1 --max=6

	**Note**: The current format is not able to support complex query such as SQL would. It would be worth looking into alternative format (or whether this is too much responsibility).

3. The dispatcher receives the query and dispatches it to any agent that can handle it
	1. The dispatching can either be 
		1. to send the received query to all agents
		2. have agents inform the dispatcher what they'd like to be notified about (*this would require a protocol*)

4. All agents **must** reply to the dispatcher, either with an empty response or with a response. The format of the response should be defined by the agent itself (think micro-services).

5. The dispatcher sends back the set of responses to the user.
