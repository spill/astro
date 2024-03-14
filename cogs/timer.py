import nextcord
from nextcord.ext import commands
import asyncio

class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def timer(self, ctx, seconds: int, *, reminder: str = None):
        if seconds <= 0:
            await ctx.send("Please provide a time that is greater than 0 seconds.")
            return 
            
        message = await ctx.send(f"Timer has been set for {seconds} seconds.")
        
        while seconds:
            await asyncio.sleep(1)
            seconds -= 1
            await message.edit(content=f"Timer: {seconds} seconds left")

        await ctx.send(f"{ctx.author.mention}, your timer is complete.")
                
        if reminder: 
            await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention}, here's your reminder: {reminder}")

def setup(bot):
    bot.add_cog(Timer(bot))
