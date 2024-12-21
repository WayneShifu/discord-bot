from discord.ext import commands

class WordChainGame(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.game_active = False
        self.previous_word = None
        self.used_words = set()

    # Helper function to check word validity
    def is_valid_word(self, word, previous):
        return previous is None or word[0].lower() == previous[-1].lower()

    @commands.command(name="start_wordchain")
    async def start_wordchain(self, ctx):
        if self.game_active:
            await ctx.send("A Word Chain game is already active!")
            return

        self.game_active = True
        self.previous_word = None
        self.used_words = set()

        instructions = (
            "🎮 **Word Chain Game Started!** 🎮\n\n"
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
        if not self.game_active:
            await ctx.send("No Word Chain game is active!")
            return

        self.game_active = False
        await ctx.send("🛑 **Word Chain Game Stopped!** 🛑")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot or not self.game_active:
            return

        word = message.content.strip().lower()

        if not message.content.startswith("$"):
            if word in self.used_words:
                await message.channel.send(f"⚠️ **{word}** has already been used!")
            elif not self.is_valid_word(word, self.previous_word):
                await message.channel.send(
                    f"❌ **{word}** doesn't start with the last letter of **{self.previous_word}**!"
                )
            else:
                self.used_words.add(word)
                self.previous_word = word
                await message.channel.send(f"✅ **{word}** accepted! Next word?")

