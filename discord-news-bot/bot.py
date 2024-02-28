import discord
from discord.ext import commands
from main import getData,getPrice
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='$', intents=intents)
@client.event
async def ready():
    print('run')


@client.command()
async def no(ctx,arg):
    temp=(arg.upper())
    arg=temp
    new=[]
    stock=[]
    new=getData(arg)        

    x=10
    while(x>0):
        
        stock.append(str(x)+': '+new[x-1])
        x-=1
    
    embed = discord.Embed(title=arg, description="Current news headlines")
    stock = '\n'.join(stock) 
    embed.add_field(name="News", value=stock)
    await ctx.send(embed=embed)
    return
@client.command()
async def price(ctx,arg):
    temp=(arg.upper())
    arg=temp
    layout=["TICKER: ","DATE: ","CHANGE: ","PRICE: ","VOLUME: ","AH/PM: "]
    stock=[]
    count=0
    for item in getPrice(arg):
        stock.append(str(layout[count])+str(item)) 
        count+=1
    new=getPrice(arg)        

    embed = discord.Embed(title=arg, description="")
    stock = '\n'.join(stock) 
    embed.add_field(name="INFO", value=stock)
    await ctx.send(embed=embed)
    return

           
@client.command() 
async def news(ctx,arg):
    temp=(arg.upper())
    arg=temp
    for item in getPrice(arg):
        await ctx.send(item)
    new=[]
    new=getData(arg)
    x=10
    while(x>0):
        
        await ctx.send(str(x)+':'+new[x-1])
        x-=1
    '''await ctx.send(stock)'''
    return 


client.run('[TOKEN]')