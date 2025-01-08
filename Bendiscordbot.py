import discord
import asyncio
import os
import random
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

# setting up intents
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

summon = False  # summon state
lactime = None  # last activity time
responses = ["Yes?", "No.", "Ugh", "Ho Ho Ho!"]  # possible responses

@client.event
async def on_ready():
    print(f"{client.user} is now online.")

@client.event
async def on_message(msg):
    global summon, lactime

    if msg.author == client.user:
        return

    # Summon Ben
    if "ben" in msg.content.lower():
        if not summon:  # prevent multiple summons
            summon = True
            lactime = datetime.now()
            await typesend(msg.channel, "Ben.")
            # unsummon verification
            asyncio.create_task(unsummon_verify(msg.channel))
    # Respond randomly if summoned
    elif summon:
        lactime = datetime.now()  # Update last activity time
        if random.random() < 0.5:  # 50% chance of response
            response = random.choice(responses)
            await typesend(msg.channel, response)

async def unsummon_verify(channel):
    global summon, lactime

    # check for inactivity
    while summon:
        await asyncio.sleep(1)
        if lactime and datetime.now() - lactime > timedelta(seconds=10):
            await typesend(channel, "Hangs up :telephone:")
            summon = False

# send message
async def typesend(channel, msg):
    async with channel.typing():  # display typing status
        await asyncio.sleep(1)  # simulate delay
        await channel.send(msg)  # output

# Run the bot with token
client.run(TOKEN)
