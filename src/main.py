# Panda-Host.de Bot for PandaNetwork

# made by 𝙿𝚊𝚗𝚍𝚊𝙼𝙲#7282 

import discord
import json
import asyncio
import secrets
import time
from discord import channel
from discord.ext import commands
from discord.flags import Intents
from time import sleep



bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
bot.remove_command('help')


# ------------------------ LOAD CONFIG ------------------------ #

with open("config.json", "r") as f:
    data = json.load(f)
    token = data["Token"]

@bot.event
async def on_ready():
    activity = discord.Game(name="Prefix: - l -help", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("[PandaHost] ----------------------------")
    print("[PandaHost]")
    print("[PandaHost] Loading Panda-Host.de by 𝙿𝚊𝚗𝚍𝚊𝙼𝙲#7282...")
    print("[PandaHost]")
    print("[PandaHost] ----------------------------")
    sleep(1)
    print(f"[PandaHost] Bot logged in as {bot.user}")


# ------------------------ COMMANDS ------------------------ #

#Help Command
@bot.command()
async def help(ctx):
    await ctx.send(':wrench: **Dieser Befehl ist in Bearbeitung!** ')


#Ping Command
@bot.command()
async def ping(ctx):
    embed=discord.Embed(color=0x676767, title='Ping Check', description=f'Mein Ping ist `{round(bot.latency * 1000)}ms`')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/896749030493814828/902943076350308432/52744pingpong_109378.png')
    await ctx.send(embed=embed)

#Info Command
@bot.command()
async def info(ctx):
    embed=discord.Embed(color=0x676767, title='Bot Infos :robot:', description='Hier findest du alle wichtigen Infos zum Bot')
    embed.add_field(name='Developer :computer:', value=' » <@710486241304641536>')
    await ctx.send(embed=embed)


#Ban Command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member=None, *, reason=None):
    if member is None:
        await ctx.send(':no_entry_sign: **Du musst einen Benutzer angeben!**')
        return
    elif reason is None:
        await ctx.send(f':no_entry_sign: **Du musst eine Begründung angeben, um {member.mention} zu kicken!**')
        return
    await member.kick(reason=reason) 
    print(f'[Command] {member} wurde mit dem Grund `{reason}` gekickt.')
    embed=discord.Embed(color=0x676767, title='Erfolgreich gekickt! :white_check_mark:', description=f'{member.mention} wurde erfolgreich mit dem Grund `{reason}` gekickt.')
    await ctx.send(embed=embed)

#Kick Command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member=None, *, reason=None):
    if member is None:
        await ctx.send(':no_entry_sign: **Du musst einen Benutzer angeben!**')
        return
    elif reason is None:
        await ctx.send(f':no_entry_sign: **Du musst eine Begründung angeben, um {member.mention} zu bannen!**')
        return
    await member.ban(reason=reason) 
    print(f'[Command] {member} wurde mit dem Grund `{reason}` gebannt.')
    embed=discord.Embed(color=0x676767, title='Erfolgreich gebannt! :white_check_mark:', description=f'{member.mention} wurde erfolgreich mit dem Grund `{reason}` gebannt.')
    await ctx.send(embed=embed)


#Server bestellen (Info)
@bot.command()
async def serverbestellen(ctx):
    embed=discord.Embed(color=0x676767, title='> **Serverbestellung**', description='Bitte fülle folgende Punkte aus:')
    embed.add_field(name='**Name:¹** \n **Email:** \n **Passwort:¹** \n\n *¹Für das Pterodactyl Interface*', value='.')
    embed.set_thumbnail(url='https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/google/298/package_1f4e6.png')
    await ctx.send(embed=embed)


#Erledigt Command





# ------------------------ EVENTS ------------------------ #

#Welcome MSG
@bot.event
async def on_member_join(member):
    channel=bot.get_channel(901047445247643668)
    embed=discord.Embed(color=0x00ff00, title=f'<:blauerpfeil:902858791069036584> {member} ist auf den Server gehüpft!', description=f'Wir freuen uns, dass du hier bist, {member.mention} ^^' f'Wir sind jetzt `{len(set(bot.users))}` Member auf diesem Server.')
    embed.set_thumbnail(url=member.avatar_url)
    await channel.send(embed=embed)

#Leave MSG
@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(901047445247643668)
    await channel.send(f'**{member} hat uns verlassen... :wave:**')

    


# ------------------------ RUN ------------------------ #


bot.run(token)

