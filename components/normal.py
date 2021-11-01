import discord
from discord.ext import commands
import math
import random
from discord_slash import cog_ext

# ! <--- Class for Basic_Calculation
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

  # ? <--- Initialize variable and function for class
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    global lcm
    def lcm(x, y) :
      if x > y:
        greater = x
      else:
        greater = y

      while(True):
        if ((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
        greater += 1
        
      return lcm

  # ? <--- Command to calculate queries from user
  @ cog_ext.cog_slash(description = "Calculate your math's query.")
  async def cal(self,ctx,query : str) :
    self.expliteral = ("").join(query)
    self.exppoet = self.expliteral.replace("*","×").replace("/", "÷")
    self.eval = eval(self.expliteral)
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exppoet}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to generate random number
  @ cog_ext.cog_slash(description = "Generate randomly selected numbers from input range.")
  async def generator(self,ctx,starting_point: float, ending_point : float) :
    self.exp = f"/generator {starting_point} {ending_point} "
    self.eval = f"{random.random(starting_point,ending_point)}"
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to square a number
  @ cog_ext.cog_slash(description = "Squared number from user.")
  async def square(self,ctx,base : float) :
    self.exp = f"{base}²"
    self.eval = f"{base ** 2}" 
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to cube a number
  @ cog_ext.cog_slash(description = "Cubed number from user.")
  async def cube(self,ctx,base : float) :
    self.exp = f"{base}³"
    self.eval = f"{base ** 3}"
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to power a base using user's exponent
  @ cog_ext.cog_slash(description = "Power the user's base to the exponent.")
  async def variable_power(self,ctx,base : float,exponent : float) :
    self.exp = f"{base} ** {exponent}"
    self.eval = f"{base ** exponent}"
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

    # ? <--- Command to square root a number
  @ cog_ext.cog_slash(description = "Square root user's number.")
  async def square_root(self,ctx,radicand : float) :
    self.exp = f"√{radicand}"
    self.eval = f"{math.sqrt(radicand)} " 
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to cube root a number
  @ cog_ext.cog_slash(description = "Cube root user's number.")
  async def cube_root(self,ctx,radicand : float) :
    self.exp = f"³√{radicand}"
    self.eval = f"{radicand ** 1./3.} "
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to root a radicand using a radical
  @ cog_ext.cog_slash(description = "Radical(root) user's radicand(number).")
  async def variable_root(self,ctx,radicand : float,radical: float) :
    self.exp = f"{radicand} ** 1/{radical}"
    self.eval = f"{radicand ** 1./radical}"
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to find factor a number
  @ cog_ext.cog_slash(description = "Find the factor of a number.")
  async def factor(self,ctx, number : int) :
    self.eval = []
    for i in range(1, number + 1) :
      if number % i == 0 :
        self.eval.append(i)
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :",value = f"Factor of `{number}`.", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to find common factor of multiple number
  @ cog_ext.cog_slash(description = "Find the common factor of multiple number.")
  async def common_factor(self,ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
        self.eval = []
        for i in range(1, min(number_1, number_2) + 1) :
          if number_1 % i == number_2 % i == 0 :
            self.eval.append(i)
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        self.embed.add_field(name = "Input :",value = f"Common Factor of `{number_1}` and `{number_2}`.", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
    else :
      self.eval = []
      for i in range(1, min(number_1, number_2, number_3) + 1) :
        if number_1 % i == number_2 % i == number_3 % i == 0 :
          self.eval.append(i)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :",value = f"Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)

  # ? <--- Command to find highest common factor of multiple number
  @ cog_ext.cog_slash(description = "Find the highest common factor of multiple number.")
  async def highest_common_factor(self,ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
      self.eval = math.gcd(number_1, number_2)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
      await ctx.send(embed = self.embed)
    else :
      self.eval = math.gcd(math.gcd(number_1, number_2), number_3)
      
  
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
      await ctx.send(embed = self.embed)

  # ? <--- Command to find multiple of a number
  @ cog_ext.cog_slash(description = "Find the multiple of a number.")
  async def multiple(self, ctx, number : int, number_range : int) :
    self.eval = []
    for i in range(1, number_range + 1) :
      self.eval.append(number * i)
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
    self.embed.add_field(name = "Input :",value = f"Multiple of `{number}`.", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.eval}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to find common multiple of multiple number
  @ cog_ext.cog_slash(description = "Find the common multiple of 2 or 3 numbers.")
  async def common_multiple(self, ctx, number_1 : int, number_2 : int, number_3 : int, number_range : int) :
    if number_3 == 0 :
      self.arr = []
      self.eval = lcm(number_1, number_2)
      for i in range(1, number_range + 1) :
        self.arr.append(self.eval * i)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.arr}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)
    else :
      self.arr = []
      self.eval = lcm(lcm(number_1, number_2), number_3)
      for i in range(1, number_range + 1) :
        self.arr.append(self.eval * i)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.arr}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)

  # ? <--- Command to find the lowest common multiple of multiple number
  @ cog_ext.cog_slash(description = "Find the lowest common multiple of 2 or 3 numbers.")
  async def lowest_common_multiple(self, ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
      self.eval = lcm(number_1, number_2)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)
    else :
      self.eval = lcm(lcm(number_1, number_2), number_3)
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)

  # ? <--- Who knows what this do ?
  @ cog_ext.cog_slash(description = "Alright, who want to kill this bot ?")
  async def terminate(self, ctx, true_or_false : str) :
    self.boolt = ["true", "t", "TRUE", "T"]
    self.boolf = ["false", "f", "FALSE", "F"]
    self.eval = ("").join(true_or_false)
    if (self.eval in self.boolt) :
      await ctx.send("Go check your dm 😈")
      await ctx.author.send("<https://m.youtube.com/watch?v=raTkZqz680Y>")
    elif (self.eval in self.boolf) :
      await ctx.send("*sigh of relief*")

# ! <--- Add Basic_Calculation into the bot
def setup(client): 
  client.add_cog(Basic_Calculation(client))