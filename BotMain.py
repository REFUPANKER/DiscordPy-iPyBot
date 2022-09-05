from email.message import Message
import BotCredential as Credential
import discord
from discord.ext import commands
import datetime
import discord.message

def BotLog(msg):
    print("[",datetime.datetime.now().strftime("%H:%M:%S"),"]",msg)

BotLog("App Started")
botIntent=discord.Intents.all()
Bot=commands.Bot(intents=botIntent,command_prefix="py ",help_command=None)
# bot run at last line

@Bot.event
async def on_ready():
    print("Bot Ready")
    BotLogChannel= Bot.get_channel(Credential.BOT_CHANNEL_LOG)
    await BotLogChannel.send("Bot Active")

@Bot.command(name="info")
async def info(ctx):
    print("info required")

@Bot.event
async def on_message(msg : Message):
    if(msg.author!=Bot.user):
        if(msg.content.startswith(Bot.command_prefix)):
            await Bot.process_commands(msg)
        

Bot.run(Credential.BOT_TOKEN)
