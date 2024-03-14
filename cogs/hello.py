import nextcord
from nextcord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # Avoid the bot responding to itself
        if message.author == self.bot.user:
            return

        # Check if the message is "hello astro", "hey astro", or "hi astro" (case-insensitive)
        if "hey astro" in message.content.lower() or "hello astro" in message.content.lower() or "hi astro" in message.content.lower():
            # Respond with a greeting, mentioning the user
            await message.channel.send(f"Hi {message.author.mention}! I'm Astro, a multi-purpose security bot developed by Ryan to assist you in various cybersecurity tasks and provide additional features.")

            # Creating and sending the embed message
            embed = nextcord.Embed(
                title="Welcome to Astro Security Bot",
                description="I am here to help you enhance your security posture and provide useful utilities. Here are some commands you can use:",
                color=0xA020F0,
            )
            embed.add_field(name="$info", value="Displays information about all available commands.", inline=False)
            embed.add_field(name="$ip <ip_address>", value="Provides geolocation information for the specified IP address.", inline=False)
            embed.add_field(name="$scan <website>", value="Conducts a security scan for the specified website.", inline=False)
            embed.add_field(name="$timer <time_amount>", value="Report any security issues or concerns to the bot's owner.", inline=False)
            embed.add_field(name="$help", value="Displays information on how to use the bot.", inline=False)
            await message.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Hello(bot))
