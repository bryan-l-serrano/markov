# markov
implements a markov-chain algorithm to text files

chain.py does the work

reddit_parser.py collects the comments of the top 25 "hot" posts
of a given subbreddit and places them in a text file to be used with 
chain.py, allowing you to "emulate" active users of a subreddit

@mkbots is a twitterbot that uses the markov chains. It selects a random subreddit every day to create markov chains from the
comments and posts chain sentences it creates every hour

a reddit bot is being considered


