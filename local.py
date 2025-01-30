import discord
import asyncio
import asyncpraw
import nest_asyncio
import os
from dotenv import load_dotenv

#this is important... for something
nest_asyncio.apply()

# Load environment variables from .env file
load_dotenv()

#Secrets
DISCORD_TOKEN=os.getenv('DISCORD_TOKEN').strip('"')
REDDIT_CLIENT_ID=os.getenv('REDDIT_CLIENT_ID').strip('"')
REDDIT_CLIENT_SECRET=os.getenv('REDDIT_CLIENT_SECRET').strip('"')
REDDIT_USER_AGENT=os.getenv('REDDIT_USER_AGENT')
CHANNEL_ID=int(os.getenv('CHANNEL_ID').strip('"'))
MONITOR_SUB=os.getenv('MONITOR_SUB').strip('"')
KEYWORDS=os.getenv('KEYWORDS').strip('"')

#split KEYWORDS string into a list, removing any whitespaces
keywords_list = [keyword.strip() for keyword in KEYWORDS.split(',')]

# Reddit API credentials and Async PRAW setup
reddit = asyncpraw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

# Intents needed to start discord client
intents = discord.Intents.default()
intents.message_content = True  # Ensure the bot can read message content

# Create a client instance of the bot
client = discord.Client(intents=intents)

async def check_keywords_notify():
    subreddit = await reddit.subreddit(MONITOR_SUB)
    while True:
        # check the 10 most recent posts
        async for submission in subreddit.new(limit=10):  # Adjust the limit if needed
            #if KEYWORDS in new title
            if any(keyword.lower() in submission.title.lower() for keyword in keywords_list):
                message = f"New post found: {submission.title}\n{submission.url}"
                print(message)
                # Send the post title to the Discord channel, print API usage
                channel = client.get_channel(CHANNEL_ID)
                if channel:
                    await channel.send(message)
                    print(f"Sent notification for: {submission.title}")
                    print(f"Rate limit: {reddit.auth.limits}\n")
        await asyncio.sleep(60)  # Check every 60 seconds

@client.event
async def on_ready():
    # This function will be called when the bot has connected to Discord
    print(f'Logged in as {client.user}')

    # Start the Reddit post-checking task
    client.loop.create_task(check_keywords_notify())  # Add the Reddit checking task to the event loop

    # Send a welcome message to the Discord channel
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Hello, Discord! I'm now online and monitoring Reddit!")

# Manually run the bot's event loop
async def main():
    await client.start(DISCORD_TOKEN)

# Use asyncio to run the main function
if __name__ == '__main__':
    asyncio.run(main())

