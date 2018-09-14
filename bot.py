
















 

bot = commands.Bot(command_prefix='c!')

 

@bot.event

async def on_ready():

    print ('I am online.')

    print('I am running as ' + bot.user.name+',''with the ID:' + bot.user.id+' and I am connected in '+str(len(bot.servers))+' servers.'' I am connected with '+str(len(set(bot.get_all_members())))+' members')

 

    await bot.change_presence(game=discord.Game(name="lilcsz#5890 | c!helps", type=1))

    print ("Started")

 
bot.run('your token')
