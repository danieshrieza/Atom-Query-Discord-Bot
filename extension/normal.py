import discord
from discord.ext import commands
import math
import random
from discord_slash import cog_ext
from datetime import datetime, timezone
from discord.ext.commands.context import Context

# ! <--- Class for Basic_Calculation --->
class Basic_Calculation(commands.Cog):

    """
    Basic_Calculation is a class that contains basic calculation command.

    Commands :
    ----------
    cal : return `str` embed

    gene : return `str` embed

    square : return `str` embed

    cube : return `str` embed

    varpower : return `str` embed

    sqrt : return `str` embed

    cbrt : return `str` embed

    varroot : return `str` embed

    factor : return `str` embed

    common_factor : return `str` embed

    highest_common_factor : return `str` embed

    multiple : return `str` embed

    common_multiple : return `str` embed

    lowest_common_multiple : return `str` embed

    terminate : return `str` embed

    """

    # ! <--- Initialize variable and function for class --->
    def __init__(self, bot):

        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

        global lcm
        def lcm(x, y) :

            if x > y :
                greater = x

            else :
                greater = y

            while(True) :

                if ((greater % x == 0) and (greater % y == 0)) :

                    lcm = greater

                    break
                
            greater += 1
            
            return lcm

    # ! <--- Command to calculate queries from user --->
    @ cog_ext.cog_slash(description = "Calculate your math's query.")
    async def cal(self, ctx : Context, query : str) :

        expliteral = ("").join(query)
        exppoet = expliteral.replace("*","×").replace("/", "÷")
        evalu = eval(expliteral)

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exppoet}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to generate random number --->
    @ cog_ext.cog_slash(description = "Generate randomly selected numbers from input range.")
    async def generator(self, ctx : Context, starting_point: float, ending_point : float) :

        exp = f"Generate number between {starting_point} and {ending_point}."
        evalu = f"{random.random(starting_point,ending_point)}"

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to square a number --->
    @ cog_ext.cog_slash(description = "Squared number from user.")
    async def square(self, ctx : Context, base : float) :

        exp = f"{base}²"
        evalu = f"{base ** 2}" 

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to cube a number --->
    @ cog_ext.cog_slash(description = "Cubed number from user.")
    async def cube(self, ctx : Context, base : float) :

        exp = f"{base}³"
        evalu = f"{base ** 3}"

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to power a base using user's exponent --->
    @ cog_ext.cog_slash(description = "Power the user's base to the exponent.")
    async def variable_power(self, ctx : Context, base : float, exponent : float) :

        exp = f"{base} ** {exponent}"
        evalu = f"{base ** exponent}"

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to square root a number --->
    @ cog_ext.cog_slash(description = "Square root user's number.")
    async def square_root(self, ctx : Context, radicand : float) :

        exp = f"√{radicand}"
        evalu = f"{math.sqrt(radicand)}" 

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to cube root a number --->
    @ cog_ext.cog_slash(description = "Cube root user's number.")
    async def cube_root(self, ctx : Context, radicand : float) :

        exp = f"³√{radicand}"
        evalu = f"{radicand ** 1./3.}"

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to root a radicand using a radical --->
    @ cog_ext.cog_slash(description = "Radical(root) user's radicand(number).")
    async def variable_root(self, ctx : Context, radicand : float, radical: float) :

        exp = f"{radicand} ** 1/{radical}"
        evalu = f"{radicand ** 1./radical}"

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to find factor a number --->
    @ cog_ext.cog_slash(description = "Find the factor of a number.")
    async def factor(self, ctx : Context, number : int) :

        evalu = []
        for i in range(1, number + 1) :
            if number % i == 0 :
                eval.append(i)

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"Factor of `{number}`.", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to find common factor of multiple number --->
    @ cog_ext.cog_slash(description = "Find the common factor of multiple number.")
    async def common_factor(self, ctx : Context, number_1 : int, number_2 : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = []
            for i in range(1, min(number_1, number_2) + 1) :
                if number_1 % i == number_2 % i == 0 :
                    eval.append(i)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"Common Factor of `{number_1}` and `{number_2}`.", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = []
            for i in range(1, min(number_1, number_2, number_3) + 1) :
                if number_1 % i == number_2 % i == number_3 % i == 0 :
                    eval.append(i)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide valid input.")

    # ! <--- Command to find highest common factor of multiple number --->
    @ cog_ext.cog_slash(description = "Find the highest common factor of multiple number.")
    async def highest_common_factor(self, ctx : Context, number_1 : int, number_2 : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = math.gcd(number_1, number_2)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}` and `{number_2}`.", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)

            await ctx.send(embed = emby_ctx)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = math.gcd(math.gcd(number_1, number_2), number_3)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide valid input.")

    # ! <--- Command to find multiple of a number --->
    @ cog_ext.cog_slash(description = "Find the multiple of a number.")
    async def multiple(self, ctx : Context, number : int, number_range : int) :

        evalu = []
        for i in range(1, number_range + 1) :
            eval.append(number * i)

        emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"Multiple of `{number}`.", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to find common multiple of multiple number --->
    @ cog_ext.cog_slash(description = "Find the common multiple of 2 or 3 numbers.")
    async def common_multiple(self, ctx : Context, number_1 : int, number_2 : int, number_range : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0 and number_range > 0) :

            arr = []
            evalu = lcm(number_1, number_2)
            for i in range(1, number_range + 1) :
                arr.append(evalu * i)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{arr}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (number_3 != None and number_1 > 0 and number_2 > 0 and number_range > 0) :

            arr = []
            evalu = lcm(lcm(number_1, number_2), number_3)
            for i in range(1, number_range + 1) :
                arr.append(evalu * i)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{arr}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide valid input.")

    # ! <--- Command to find the lowest common multiple of multiple number --->
    @ cog_ext.cog_slash(description = "Find the lowest common multiple of 2 or 3 numbers.")
    async def lowest_common_multiple(self, ctx : Context, number_1 : int, number_2 : int, number_3 : int) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = lcm(number_1, number_2)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = lcm(lcm(number_1, number_2), number_3)

            emby_ctx = discord.Embed(title = "Math Query", description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(179, 27, 27))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide valid input.")

# ! <--- Add Basic_Calculation into the bot --->
def setup(bot): 
  bot.add_cog(Basic_Calculation(bot))