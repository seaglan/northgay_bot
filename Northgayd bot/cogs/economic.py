import discord
from discord.ext import commands
from datetime import datetime, date, time

client = commands.Bot(command_prefix = "!", intents = discord.Intents.all())


class Economic(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.collection = self.cluster.bloodsbank.bloodscollection

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == self.client.user:
			return

		user = message.author
		data = self.collection.find_one({"_id": user.id})


	@commands.command(
		name = "Топ 3 игры",
		aliases = ["gamelist6", "gamelist6"],
		brief = "выбор/бан из 6 игр с итогом в топ 3",
		usage = "gamelist6 <@user> <@user> <@user>..."
	)
	async def gamelist6(self, ctx, member1: discord.Member, member2: discord.Member, member3: discord.Member):
		
        while list_one.author =! member1:
            await client.wait_for_message(content=('m!mode computer' or 'm!mode player'))
            gamelist = self.collection.find_one({"_id": member.id})["balance"]

        self.collection.update_one({"_id": member.id},
            {"$set": {"balance": mbalance + amount}})

        self.collection.update_one({"_id": member.id},
            {"$set": {"weekbalance": mweekbalance + amount}})
        print (f"{datetime.today()}||{ctx.message.author} изменил баланс пользователя {member.name}#{member.id} на {amount}")
        await ctx.message.add_reaction("🩸")



def setup(client):
	client.add_cog(Economic(client))