from nextcord import Interaction, Embed, ButtonStyle
import nextcord
from nextcord.ui import Button, View

class CloseButton(View):
    def __init__(self):
        super().__init__()
        self.add_item(Button(label="Close", style=ButtonStyle.red, emoji="❌", custom_id="close_btn"))

    @nextcord.ui.button(label="Close", style=ButtonStyle.red, emoji="❌")
    async def close(self, button: Button, interaction: Interaction):
        await interaction.message.delete()