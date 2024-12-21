from discord.ext import commands

class WordChainGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_games = {}  # Tracks active games by channel ID

    # Helper function to check word validity
    def is_valid_word(self, word, previous):
        return previous is None or word[0].lower() == previous[-1].lower()

    @commands.command(name="start_wordchain")
    async def start_wordchain(self, ctx):
        """Starts a Word Chain game in the current channel."""
        if ctx.channel.id in self.active_games:
            await ctx.send("There's already an active Word Chain game in this channel!")
            return

        self.active_games[ctx.channel.id] = {
            "previous_word": None,
            "used_words": set(),
        }

        instructions = (
            "🎮 **Word Chain Game Started in this Channel!** 🎮\n\n"
            "**How to Play:**\n"
            "1️⃣ The game starts with the first word sent by any player.\n"
            "2️⃣ Each subsequent word must begin with the last letter of the previous word.\n"
            "3️⃣ Words cannot be repeated!\n"
            "4️⃣ No special characters, numbers, or spaces are allowed—just plain words.\n\n"
            "Type your first word to begin! 🌟"
        )
        await ctx.send(instructions)

    @commands.command(name="stop_wordchain")
    async def stop_wordchain(self, ctx):
        """Stops the Word Chain game in the current channel."""
        if ctx.channel.id not in self.active_games:
            await ctx.send("No Word Chain game is active in this channel!")
            return

        del self.active_games[ctx.channel.id]
        await ctx.send("🛑 **Word Chain Game Stopped in this Channel!** 🛑")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or message.channel.id not in self.active_games:
            return

        game = self.active_games[message.channel.id]
        word = message.content.strip().lower()

        # Ignore commands
        if word.startswith("$"):
            return

        # Validate word
        if word in game["used_words"]:
            await message.channel.send(f"⚠️ **{word}** has already been used!")
        elif not self.is_valid_word(word, game["previous_word"]):
            await message.channel.send(
                f"❌ **{word}** doesn't start with the last letter of **{game['previous_word']}**!"
                if game["previous_word"]
                else "❌ Start with any word!"
            )
        else:
            # Valid word
            game["used_words"].add(word)
            game["previous_word"] = word
            await message.channel.send(f"✅ **{word}** accepted! Next word?")
