from discord.ext import commands
from env import TRAVIS_TOKEN
bot = commands.Bot(command_prefix="travis!")

COGS = ['generate']

for cog in COGS:
    bot.load_extension(f"commands.{cog}")

@bot.event
async def on_ready():
    print(f"Bot has logged in as {bot.user}!")

bot.run(TRAVIS_TOKEN)