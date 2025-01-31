# Subreddit Scanner Discord Bot

A discord bot that monitors a subreddit of your choosing and messages a discord channel whenever a new post with your keywords is found. Uses free OAUTH Reddit API token and asyncio with discord bots.

## Setup
1. Create a script at https://old.reddit.com/prefs/apps to get your API Key and Client
   * Client_ID is under "personal use script", Client_Secret = secret
2. Create a discord channel and copy the channel ID
   * If you don't see the copy channel id right click option, you need to enable dev mode 
3. Create a discord bot and add to your channel with message privileges and message content intentions
   * https://discord.com/developers/applications > new application
   * Copy your token (discord_token) or generate/copy a new one in the bot menu
   * Navigate to bot > priveleged gateway intents and check ```Message Content Intent```
   * Then go to OAuth2 > URL generator select bot scope > bot permissions send messages > guild install
   * Paste your generated URL and add your bot to your server. Make sure it can access your designated channel

## Environment
These are the variables you will need to run the script:
```yml
    environment:
      - DISCORD_TOKEN="yourtoken"
      - REDDIT_CLIENT_ID="yourid"
      - REDDIT_CLIENT_SECRET="yoursecret"
      - REDDIT_USER_AGENT="youragent"
      - CHANNEL_ID="yourid"
      - MONITOR_SUB="subreddit" #no r/, just the name
      - KEYWORDS="list, of, keywords"
```
User agent: ```<platform>:<app ID>:<version string> (by u/<Reddit username>)``` 
* For example, ```android:com.example.myredditapp:v1.2.3 (by u/kemitche)```


## Installation
There are 3 ways of running the service:
- Using docker compose (recommended)
- Building docker locally
- Running the python script locally

### Docker Compose
Run the above compose file and fill in the environment variables. That's it!

~~### Building Docker Locally
Download all files above into 1 directory. You will need to point to .env file and fill in the same variables in your run command.~~ 

### Python Script
Uses python 3.13, modules needed are in requirements.txt

## Usage
* Every 60 seconds, the script will check the 10 most recent posts from your subreddit for keywords
* When it finds a matching post, your discord bot will post the title + URL for the post
* Create a new instance of the script for every additional subreddit you want to monitor

The scripts stays well below Reddit's 100 calls per minute free tier and you can see your usage within the container logs

If you have any questions/suggestions or just need some help running/using the bot, you can raise an issue or message me on reddit at u/Resolute_Pecan.
