import nextcord
from nextcord.ext import commands
import asyncio

class Reminder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reminder(self, ctx, time: str, *, reminder: str = None):
        time_units = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
            'w': 604800
        }

        unit = time[-1]
        if unit not in time_units:
            await ctx.send("Invalid time unit. Please use 's', 'm', 'h', 'd', or 'w'.")
            return

        try:
            duration = int(time[:-1]) * time_units[unit]
        except ValueError:
            await ctx.send("Invalid time format. Please provide a number followed by a valid time unit ('s', 'm', 'h', 'd', 'w').")
            return

        if duration <= 0:
            await ctx.send("Please provide a time greater than 0.")
            return

        message_content = f"🕐 Timer has been set for {duration} seconds.\n"
        if reminder:
            message_content += f"🔔 Reminder: {reminder}"
            
        embed = nextcord.Embed(
            title="Reminder",
            description=message_content,
            color=0xA020F0
        )

        message = await ctx.send(embed=embed)

        while duration:
            await asyncio.sleep(1)
            duration -= 1
            embed.description = f"🕐 Timer: {duration} seconds left.\n{message_content.splitlines()[-1]}"
            await message.edit(embed=embed)

        await ctx.send(f"{ctx.author.mention}, your timer is complete.")
                
        if reminder: 
            await asyncio.sleep(1)
            await ctx.send(f"{ctx.author.mention}, here's your reminder: {reminder}")

def setup(bot):
    bot.add_cog(Reminder(bot))
