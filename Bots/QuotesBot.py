from discord.ext import commands

from Utils.Quotes import Quotes


class QuotesBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.register_commands()

    def register_commands(self):
        @self.bot.command(name='quote')
        async def random_quote(ctx):
            quote = Quotes("random").get_quote()
            await ctx.send(quote)

        @self.bot.command(name='todayQuote')
        async def today_quote(ctx):
            quote = Quotes('today').get_quote()
            await ctx.send(quote)
