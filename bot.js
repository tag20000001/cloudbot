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

 
bot.run('your token')
