from nextcord import Interaction
import nextcord
from nextcord.ext import commands
import math
from datetime import datetime, timezone
from config import guild_id


# NOTE : Class for Line
class Line(commands.Cog) :


    # NOTE : Initialize parameter for class 
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate distance between two points on a Cartesian Plane 
    @ nextcord.slash_command(
        description = "Calculate the distance between two points."
    )

    async def distance_between_two_points(self, ctx : Interaction, x_2 : float, x_1 : float, y_2 : float, y_1 : float) :

        exp = f"√({x_2} - {x_1})² + ({y_2} - {y_1})²"
        evalu = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

        embed_msg = nextcord.Embed(
            title = "Cartesian Query", 
            description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate gradient of a line 
    @ nextcord.slash_command(
        description = "Calculate the gradient of a line."
    )

    async def gradient_of_a_line(self, ctx : Interaction, y_2 : float, y_1 : float, x_2 : float, x_1 : float) :

        exp = f"{y_2} - {y_1} ÷ {x_2} - {x_1}"
        evalu = (y_2 - y_1) / (x_2 - x_1)

        embed_msg = nextcord.Embed(
            title = "Cartesian Query", 
            description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the midpoint of a line 
    @ nextcord.slash_command( 
        description = "Calculate the midpoint of a line."
    )

    async def midpoint_of_a_line(self, ctx : Interaction, x_1 : float, x_2 : float, y_1 : float, y_2 : float) :

        exp = f"(({x_1} + {x_2}) ÷ 2, ({y_1} + {y_2}) ÷ 2)"
        evalu = ((x_1 + x_2) / 2, (y_1 + y_2) / 2)

        embed_msg = nextcord.Embed(
            title = "Cartesian Query", 
            description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add Line to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(Line(bot))