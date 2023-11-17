import discord
import os 
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['DISCORD_API']

# Initialize Discord client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user.name} is online!")


@client.event
async def on_message(message):
    print(f"Message received from {message.author}: {message.content}")

    if message.author == client.user:
        return


    content = message.content.strip()

    if content.startswith("https://twitter.com/"):
        embed_rul="https://vxtwitter.com/"+content.split('https://twitter.com/')[1]
        print(embed_rul)
    elif content.startswith("https://x.com/"):
        embed_rul="https://vxtwitter.com/"+content.split('https://x.com/')[1]
        print(embed_rul)
    else:
        return

    await message.reply(embed_rul)

client.run(os.environ['DISCORD_API'])