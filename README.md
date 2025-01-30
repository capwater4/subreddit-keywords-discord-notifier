# Subreddit Scanner Discord Bot

A discord bot that monitors a subreddit of your choosing and messages a discord channel whenever a new post with your keywords is found. Uses free OAUTH Reddit API token and asyncio with discord bots.

## Setup
1. Create a script at https://old.reddit.com/prefs/apps to get your API Key and Client
2. Create a discord channel and copy the channel ID
3. Create a discord bot with message privileges and message content intentions

## Installation
There are 3 ways of running the service:
- Using docker compose (recommended)
- Building docker locally
- Running the python script locally

### Docker Compose
Run the above compose file and fill in the environment variables. That's it!

### Building Docker Locally
Download all files above into 1 directory. You will need to point to .env file and fill in the same variables in your run command. 

### Python Script
Uses python 3.13, modules needed are in requirements.txt


If you have any questions/suggestions or just need some help running/using the bot, you can raise an issue or message me on reddit at u/Resolute_Pecan.
