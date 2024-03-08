import nextcord
from nextcord.ext import commands
import requests

class ip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api_key = "9d14c1137000410780ccdc12432600c1e916f9fad6afac29c6a5c2f2"

    # Correctly decorate the command method within the cog
    @commands.command()
    async def ip(self, ctx, ip_address: str):
        url = f"https://api.ipdata.co/{ip_address}"
        response = requests.get(url, params={"api-key": self.api_key})
        if response.status_code == 200:
            data = response.json()
            embed = nextcord.Embed(
                title=f"IP Location for {ip_address}",
                description="Information is generalized:",
                color=0xA020F0
            )
            embed.add_field(name="Country", value=data['country_name'], inline=True)
            embed.add_field(name="Region", value=data['region'], inline=True)
            embed.add_field(name="City", value=data['city'], inline=True)
            embed.add_field(name="IP", value=data['ip'], inline=False)
            embed.add_field(name="ISP", value=data.get('asn', {}).get('name', 'N/A'), inline=True)
            embed.add_field(name="Time Zone", value=data.get('time_zone', {}).get('name', 'N/A'), inline=True)
            embed.add_field(name="Threat Level", value='Yes' if data.get('threat', {}).get('is_threat') else 'No', inline=True)
            embed.add_field(name="Bot Status", value='Yes' if data.get('threat', {}).get('is_bot') else 'No', inline=True)
            
            # Optionally set thumbnail, author, etc.
            embed.set_footer(text="Astro Security Bot | Developed by x_x0010")

            await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to retrieve data. Make sure the IP address is valid.")

def setup(bot):
    bot.add_cog(ip(bot))