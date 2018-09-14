#pylint:disable=E0001

import discord

import asyncio

from discord.ext.commands import bot

from discord.ext import commands

import platform

import time

import random

from PIL import ImageSequence

from PIL import Image

from io import BytesIO

import aiohttp

from os import path

import os

import datetime

import json

import sys

import os

import re

import string

import traceback

import io

import inspect

import random

import functools

import textwrap

from urllib.parse import urlparse

from contextlib import redirect_stdout

discord.__version__

'1.0.0a'

 

bot = commands.Bot(command_prefix='c!')

 

@bot.event

async def on_ready():

    print ('I am online.')

    print('I am running as ' + bot.user.name+',''with the ID:' + bot.user.id+' and I am connected in '+str(len(bot.servers))+' servers.'' I am connected with '+str(len(set(bot.get_all_members())))+' members')

 

    await bot.change_presence(game=discord.Game(name="lilcsz#5890 | c!helps", type=1))

    print ("Started")

 

@bot.command()

async def ping():

    await bot.say('so? ')  

 

@bot.command(pass_context=True)

async def avatar(ctx, user: discord.Member):

 await bot.say('https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024'.format(user))

 

@bot.command()

async def russian():

  await bot.say('vodka')

   

@bot.command()  

async def rage():

    await bot.say('idiots reeeeeeee')

 

@bot.command()

async def hi():

    await bot.say('**Hi! welcome**')  

    

@bot.command(pass_context=True)

async def kick(ctx, user: discord.Member):

    author = ctx.message.author

    if author.server_permissions.kick_members:

        await bot.kick(user)

        await bot.say("{} has been kicked!".format(user.name))

    else:

        await bot.say("You do **NOT** have permission to run this command!")

 

@bot.command(pass_context=True)

async def ban(ctx, user: discord.Member):

    author = ctx.message.author

    if author.server_permissions.ban_members:

        await bot.ban(user)

        await bot.say("{} has been banned!".format(user.name))

    else:

        await bot.say("You do **NOT** have permission to run this command! sad :l")           

 

@bot.command(pass_context=True)

async def ownerbot(ctx):

   embed = discord.Embed(name="Cloud Bot", description="Bot Owner is: lilcsz#5890 send DM for help.", color=0xff00f6)

   await bot.say(embed=embed)

 

@bot.command()

async def say(*, content):

        await bot.say(content) 

    

@bot.command(pass_context = True)

async def userinfo(ctx, user: discord.Member):

   embed = discord.Embed(name="Users Info!", description="Here's what I could find about the user.", color=0xff00f6)

   embed.set_author(name="{}'s info.".format(user.name))

   embed.add_field(name="Users Name", value=user.name, inline=True)

   embed.add_field(name="Users ID", value=user.id, inline=True)

   embed.add_field(name="Users Status", value=user.status, inline=True)   

   embed.add_field(name="Users Joined at", value=user.joined_at, inline=True)  

   await bot.say(embed=embed)                             

@bot.command(pass_context = True)

async def mute(ctx, member: discord.Member):

     if ctx.message.author.server_permissions.kick.members or ctx.message.author.id == '194151340090327041':

        role = discord.utils.get(member.server.roles, name='Muted')

        await bot.add_roles(member, role)

        embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)

        await bot.say(embed=embed)

     else:

        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)

        await bot.say(embed=embed)        

        

@bot.command(pass_context = True)

async def givemod(ctx, member: discord.Member):

     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':

        role = discord.utils.get(member.server.roles, name='Moderator')

        await bot.add_roles(member, role)

        embed=discord.Embed(title="User Moderator now!", description="**{0}** is get Moderator role from **{1}**!".format(member, ctx.message.author), color=0xff00f6)

        await bot.say(embed=embed)

     else:

        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)

        await bot.say(embed=embed)       

        

@bot.command(pass_context=True)

async def delmod(ctx, member: discord.Member):

     if ctx.message.author.server_permissions.mute_members:

        role = discord.utils.get(member.server.roles, name='Moderator')

        await bot.remove_roles(member, role)

        embed=discord.Embed(title="User Not Moderator Now!", description="**{0}** is not Moderator now!".format(member, ctx.message.author), color=0x6b009c)

        await bot.say(embed=embed)

     else:

        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)

        await bot.say(embed=embed)        

                

@bot.command(pass_context=True)

async def deletethis(ctx):

    await bot.say('Ok!')

    await bot.delete_message(ctx.message)

    await bot.say('**Message deleted!**')

 

@bot.command(pass_context=True)

async def clear(ctx, number):

    mgs = [] #Empty list to put all the messages in the log

    number = int(number) #Converting the amount of messages to delete to an integer

    async for x in bot.logs_from(ctx.message.channel, limit = number):

        mgs.append(x)

    await bot.delete_messages(mgs)                                                                            

@bot.command(pass_context=True)

async def helps(ctx):

   embed = discord.Embed(name="Cloud Bot", description="You can look at the commands here! c!clear Clear message! limit 100 (c!clear) c!ban Ban member! c!kick Kick member ! c!say (c!say text) c!mute Mute member! c!deletethis Delete 1 message! c!ownerbot See bot owner! c!userinfo See member info c!invitebot Invite bot! c!givemod Give moderator! c!delmod Delete mod role from user c!help_mod Help moderator commands c!unmute Unmute member!", color=0xff0000)

   await bot.say(embed=embed)

   

@bot.command(pass_context=True)

async def help_mod(ctx):

 embed = discord.Embed(name="Mod", description="Moderator Commands Help! ------------ c!givemod - You need do create Moderator role not mod, moderator only Moderator role and c!givemod user ------------ c!delmod - You need say c!delmod user ------------ c!mute - You need create Muted role and say c!mute user (permission kick members) ------------ c!unmute - Say c!unmute user", color= 0x00FF00)

 await bot.say(embed=embed)            

   

   

   

   

   

   

 

@bot.command(pass_context=True)

async def invitebot(ctx):

   embed = discord.Embed(name="Cloud Bot", description="Invite bot here: https://goo.gl/eWhCmz", color=0xff0000)

   await bot.say(embed=embed)   

 

@bot.command(pass_context=True)

async def unmute(ctx, member: discord.Member):

     if ctx.message.author.server_permissions.mute_members:

        role = discord.utils.get(member.server.roles, name='Muted')

        await bot.remove_roles(member, role)

        embed=discord.Embed(title="User Unmuted!", description="**{0}** is unmuted!".format(member, ctx.message.author), color=0x6b009c)

        await bot.say(embed=embed)

     else:

        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command, Fool", color=0x6b009c)

        await bot.say(embed=embed)          

bot.run("botToken") 

