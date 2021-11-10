import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())


@client.event
async def on_ready():
	print("Bot connected to the server")


@client.event
async def on_command_error(ctx, error):
	print(error)

	if isinstance(error, commands.UserInputError):
		await ctx.send(embed = discord.Embed(
			description = f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief}): `{ctx.prefix}{ctx.command.usage}`"
		))


@client.command()
@commands.is_owner()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	client.load_extension(f"cogs.{extension}")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")


client.run("TOKEN")