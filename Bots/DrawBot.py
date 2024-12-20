import random
from discord.ext import commands

class DrawBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.register_commands()

    def register_commands(self):
        @self.bot.command(name='luckyDraw')
        @commands.has_permissions(administrator=True)  # Correct decorator
        async def draw_member(ctx):
            members = [member for member in ctx.guild.members if not member.bot]

            if members:
                # Print all members included in the draw
                member_names = [member.name for member in members]
                member_list = ', '.join(member_names)
                print(f'Members included in the draw: {member_list}')

                # Select a random winner
                winner = random.choice(members)
                await ctx.send(f'Congratulations {winner.mention}! You are the lucky one today!')
            else:
                await ctx.send('No members found to draw from.')

        @draw_member.error
        async def draw_error(ctx, error):
            if isinstance(error, commands.MissingPermissions):
                await ctx.send('You do not have the necessary Administrator permission(s) to run this command.')
            else:
                await ctx.send('Something went wrong while doing the drawing!')
