from discord.ext import commands
from Utils.RandomGiphy import RandomGiphy

class GiphyResponder(commands.Cog):
    def __init__(self, bot, giphy_api_key):
        self.bot = bot
        self.giphy_api_key = giphy_api_key

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Use the RandomGiphy utility to send a GIF if needed
        await RandomGiphy(self.giphy_api_key, message).send()
