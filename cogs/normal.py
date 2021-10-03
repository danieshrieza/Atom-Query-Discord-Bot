import discord
from discord.ext import commands
import math
import random
from discord_slash import cog_ext

class Basic_Calculation(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

  @ cog_ext.cog_slash(description = "Calculate your math's query.")
  async def cal(self,ctx,query : str) :
    self.exp = ("").join(query)
    self.evalu = eval(self.exp)
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Generate randomly selected numbers from input range.")
  async def generator(self,ctx,starting_point: float, ending_point : float) :
    self.exp = f"/generator {starting_point} {ending_point} "
    self.evalu = f"{random.random(starting_point,ending_point)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Squared number from user.")
  async def square(self,ctx,base : float) :
    self.exp = f"{base} ** 2"
    self.evalu = f"{base ** 2}" 
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Cubed number from user.")
  async def cube(self,ctx,base : float) :
    self.exp = f"{base} ** 3 "
    self.evalu = f"{base ** 3}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Power the user's base to the exponent.")
  async def varpower(self,ctx,base : float,exponent : float) :
    self.exp = f"{base} ** {exponent}"
    self.evalu = f"{base ** exponent}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Square root user's number.")
  async def sqrt(self,ctx,radicand : float) :
    self.exp = f"{radicand} ** 1/2 "
    self.evalu = f"{math.sqrt(radicand)} " 
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Cube root user's number.")
  async def cbrt(self,ctx,radicand : float) :
    self.exp = f"{radicand} ** 1/3"
    self.evalu = f"{radicand ** 1./3.} "
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Radical(root) user's radicand(number).")
  async def varroot(self,ctx,radicand : float,radical: float) :
    self.exp = f"{radicand} ** 1/{radical}"
    self.evalu = f"{radicand ** 1./radical}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the factor of a number.")
  async def factor(self,ctx, number : int) :
    self.evalu = []
    for i in range(1, number + 1) :
      if number % i == 0 :
        self.evalu.append(i)
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"Factor of `{number}`.", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the common factor of multiple number.")
  async def common_factor(self,ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
        self.evalu = []
        for i in range(1, min(number_1, number_2) + 1) :
          if number_1 % i == number_2 % i == 0 :
            self.evalu.append(i)
        self.User = ctx.author
        self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :",value = f"Common Factor of `{number_1}` and `{number_2}`.", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
    else :
        self.evalu = []
        for i in range(1, min(number_1, number_2, number_3) + 1) :
          if number_1 % i == number_2 % i == number_3 % i == 0 :
            self.evalu.append(i)
        self.User = ctx.author
        self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :",value = f"Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the highest common factor of multiple number.")
  async def highest_common_factor(self,ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
      self.evalu = math.gcd(number_1, number_2)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
      await ctx.send(embed = self.embed)
    else :
      self.evalu = math.gcd(math.gcd(number_1, number_2), number_3)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
      await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the multiple of a number.")
  async def multiple(self, ctx, number : int, number_range : int) :
    self.evalu = []
    for i in range(1, number_range + 1) :
      self.evalu.append(number * i)
    self.User = ctx.author
    self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"Multiple of `{number}`.", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the common multiple of 2 or 3 numbers.")
  async def common_multiple(self, ctx, number_1 : int, number_2 : int, number_3 : int, number_range : int) :
    if number_3 == 0 :
      self.arr = []
      self.evalu = math.lcm(number_1, number_2)
      for i in range(1, number_range + 1) :
        self.arr.append(self.evalu * i)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.arr}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)
    else :
      self.arr = []
      self.evalu = math.lcm(number_1, number_2, number_3)
      for i in range(1, number_range + 1) :
        self.arr.append(self.evalu * i)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.arr}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Find the lowest common multiple of 2 or 3 numbers.")
  async def lowest_common_multiple(self, ctx, number_1 : int, number_2 : int, number_3 : int) :
    if number_3 == 0 :
      self.evalu = math.lcm(number_1, number_2)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)
    else :
      self.evalu = math.lcm(number_1, number_2, number_3)
      self.User = ctx.author
      self.embed = discord.Embed(title = "Math Query", colour = discord.Color.from_rgb(172, 209, 175))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Alright, who want to kill this bot ?")
  async def terminate(self, ctx, true_or_false : str) :
    self.evalu = ("").join(true_or_false)
    if (self.evalu.lower() == ("true" or "t")) or (self.evalu.upper() == ("TRUE" or "T")) :
      await ctx.send("Go check your dm.")
      await ctx.author.send("<https://m.youtube.com/watch?v=raTkZqz680Y>")
    elif (self.evalu.lower() == ("false" or "f")) or (self.evalu.upper() == ("FALSE" or "F")) :
      await ctx.send("*sigh of relief*")

def setup(client):
  client.add_cog(Basic_Calculation(client))