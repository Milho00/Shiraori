import discord
from discord.ext import commands, tasks

PREFIX = '.'

client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')

# Shirochka
@client.event

async def on_ready():
	print('Connected')

	await client.change_presence(status = discord.Status.online)
	await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = 'Music'))


# Delete
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def clear(ctx, amount=100):
	await ctx.channel.purge(limit = amount)

# Kick
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def kick(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.kick(reason = reason)
	await ctx.send(f'kick user { member.mention }')

# Ban
@client.command(pass_context = True)
@commands.has_permissions(administrator = True)

async def ban(ctx, member: discord.Member, *, reason = None):
	await ctx.channel.purge(limit = 1)

	await member.ban(reason = reason)
	await ctx.send(f'ban user { member.mention }')

# Command help
@client.command(pass_context = True)

async def help(ctx):
	await ctx.channel.purge(limit = 1)
	emb = discord.Embed(title='Commands:', colour = discord.Colour.dark_red())

	emb.add_field(name = '{}clear'.format(PREFIX), value = 'Clear text')
	emb.add_field(name = '{}ban'.format(PREFIX), value = 'Ban user')
	emb.add_field(name = '{}kick'.format(PREFIX), value = 'Kick user')

	#emb.set_footer(text = ctx.author.name, icon_url = ctx.author.avatar_url) чтобы показывало снизу кто ввел команду

	await ctx.send(embed = emb)

# Token
token = open('token.txt', 'r').readline()

client.run(token)