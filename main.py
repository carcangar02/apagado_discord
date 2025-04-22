import subprocess
import discord
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path="tokens.env")  

TOKEN = os.getenv("TOKEN")


TIEMPO_LIMITE_SEGUNDOS = 10

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)




@client.event
async def on_message(message):
    if message.author == client.user:
        return  

    if message.content.lower() == "apagar":
        await message.channel.send("Apagando el PC... Buenas Noches Carlos")
        await subprocess.call("shutdown /s /t 1", shell=True)

client.run(TOKEN)
