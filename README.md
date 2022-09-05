# DiscordPy - iPyBot [Open Source Discord Bot]
iPyBot - Bot for Discord 
### installation
[DiscordPy](https://discordpy.readthedocs.io/en/stable/)
```python
python -m pip install discord.py
```

## Critical Info about commands :
1- Bot Intent requires all intents in program 
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
4- File for Bot credential and Room IDs and more


<img width="468" height="168" align="left" src="https://user-images.githubusercontent.com/68808212/188504884-543fd8cd-9679-402e-929c-66acc4eb37e2.png"/>
