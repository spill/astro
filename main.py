import nextcord
import os
from nextcord.ext import commands
from dotenv import load_dotenv

load_dotenv('config.env')

intents = nextcord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Streaming(name="astro bot", url="https://twitch.tv/astro_bot"))
    print("Bot is now set to streaming status.")
    print(f"hello, this is a bot made by ryan {bot.user.name} ({bot.user.id})")
    print('___________________________________________________________________')
    

# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(os.getenv('TOKEN'))