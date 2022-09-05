# DiscordPy - iPyBot
iPyBot - Bot for Discord 
### installation
[DiscordPy](https://discordpy.readthedocs.io/en/stable/)
```python
python -m pip install discord.py
```

## Critical Info about commands :
1- Bot Intent required all intents in program 
```python
botIntent=discord.Intents.all()
Bot=commands.Bot(intents=botIntent,command_prefix="py ",help_command=None)
```
2- Adding "on_message" event require to use Bot."proccess_command"

3- Also adding "on_message" event require to check message author isnt our bot
```python
@Bot.event
async def on_message(msg : Message):
    if(msg.author!=Bot.user):
        if(msg.content.startswith(Bot.command_prefix)):
            await Bot.process_commands(msg)
```
