import nextcord
from nextcord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Correctly decorate the command method within the cog
    @commands.command()
    async def info(self, ctx):
        
        ctx.send("This is an info command for ryan's astro bot")
        
        embed = nextcord.Embed(
            title="Test Embed",
            description="Test Embed 2",
            color=0x00ff00
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Basic(bot))
