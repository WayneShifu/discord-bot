import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

from Bots.DrawBot import DrawBot
from Bots.GiphyResponder import GiphyResponder
from Bots.WordChainGame import WordChainGame
from Handlers.EventHandler import EventHandler
from Bots.QuotesBot import QuotesBot
import asyncio

# Load environment variables from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GIPHY_API_KEY = os.getenv('GIPHY_API_KEY')

# Intents for the bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Initialize the bot with a command prefix
bot = commands.Bot(command_prefix='$', intents=intents)

class HelloMyFriendBot:
    def __init__(self, bot, giphy_api_key):
        self.bot = bot
        self.giphy_api_key = giphy_api_key

        coro = self.setup()
        asyncio.run(coro)
        EventHandler(self.bot, GIPHY_API_KEY)

    async def setup(self):
        await self.bot.add_cog(GiphyResponder(self.bot, self.giphy_api_key))
        await self.bot.add_cog(QuotesBot(self.bot))
        await self.bot.add_cog(DrawBot(self.bot))
        await self.bot.add_cog(WordChainGame(self.bot))

    def run(self):
        self.bot.run(DISCORD_TOKEN)

if __name__ == '__main__':
    if DISCORD_TOKEN is None or GIPHY_API_KEY is None:
        print("Environment variables for DISCORD_BOT_TOKEN or GIPHY_API_KEY are not set.")
    else:
        discordBot = HelloMyFriendBot(bot, GIPHY_API_KEY)
        discordBot.run()
