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
            title="Astro Info Menu",
            description="Commands\n$info - offers a comprehensive outline of all of astro's commands.\n#ip <ip_address> - provides geolocation of IP Address",
            color=0xA020F0
        )
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Basic(bot))
