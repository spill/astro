import nextcord
from nextcord.ext import commands
import socket

class PortScanner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def scan(self, ctx, ip: str, start_port: int, end_port: int):
        """Scans for open TCP ports on a given IP address within the specified port range."""
        if end_port > 65535:  # TCP ports range from 1 to 65535
            await ctx.send("Invalid end port. TCP ports range from 1 to 65535.")
            return

        await ctx.send(f"Initializing scan on IP: {ip} from ports {start_port} to {end_port}. This process may take time depending on how many ports are being scanned.")

        port_services = {
            21: 'FTP',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            3306: 'MySQL',
            3389: 'RDP',
            5060: 'SIP',
            8080: 'HTTP-Proxy'
        }
        
        open_ports = []
        for port in range(start_port, end_port + 1):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(1)  # Timeout for each attempt to connect
                    result = s.connect_ex((ip, port))
                    if result == 0:
                        service = port_services.get(port, 'Unknown service')
                        open_ports.append((port, service))
            except Exception as e:
                await ctx.send(f"An error occurred during scanning: {e}")
                return

        embed = nextcord.Embed(
            title=f"Scan Results for {ip}",
            description=f"Scanned ports {start_port} to {end_port}.",
            color=0xA020F0
        )
        
        if open_ports:
            ports_str = '\n'.join(f"Port {port}: {service}" for port, service in open_ports)
            embed.add_field(name="Open Ports", value=ports_str, inline=False)
        else:
            embed.add_field(name="Open Ports", value="No open ports found.", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(PortScanner(bot))
