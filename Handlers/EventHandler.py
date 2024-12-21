import discord

from Utils.RandomGiphy import RandomGiphy


class EventHandler:
    def __init__(self, _bot, giphy_api_key):
        self.bot = _bot
        self.giphy_api_key = giphy_api_key
        self.register_events()

    def register_events(self):
        @self.bot.event
        async def on_ready():
            print(f'We have logged in as {self.bot.user}')

        @self.bot.event
        async def on_message(message):
            if message.author == self.bot.user:
                return

            # Check if the message is in a DM or a guild channel
            if isinstance(message.channel, discord.DMChannel):
                print(f"DM from {message.author}: {message.content}")
            else:
                # Print the channel name
                channel = message.channel
                print(f"Message from {message.author} in channel {channel.name}: {message.content}")

            # Check if the message is a valid command
            if message.content.startswith('$'):
                ctx = await self.bot.get_context(message)
                if ctx.command is None:
                    available_commands = ', '.join([command.name for command in self.bot.commands])
                    await message.channel.send(f"Available commands: {available_commands}")
                else:
                    # Allow the bot to process commands
                    await self.bot.process_commands(message)