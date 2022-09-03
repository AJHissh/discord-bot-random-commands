import lightbulb
import hikari
from datetime import date
import urllib.parse
from dotenv import load_dotenv
import os

import typing

import re


load_dotenv()

TOKEN = os.environ["TOKEN"]

today = date.today()
prefix = "!"
bot = lightbulb.BotApp(token=TOKEN, default_enabled_guilds=(1009546108042756117), prefix=prefix)


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot is up and running...')
    
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)
    if event.content == ('good morning bot'):
        await event.message.respond(f'Jolly good morning to you govnah {event.author.mention}')
    if event.content == ('good morning Botfrag'):
        await event.message.respond(f'Rise and shine! {event.author.mention}')
    if event.content == ('good morning'):
        await event.message.respond(f'Coffee or Tea {event.author.mention}?')
    if event.content == ('Good morning '):
        await event.message.respond(f'Morning{event.author.mention}!')
    if event.content == ('Good job bot'):
        await event.message.respond(f'I am at your service {event.author.mention}')
    if event.content == ('Good job Bot'):
        await event.message.respond(f'Thank you {event.author.mention}!')
    if ('.youtube') in event.content:
       query = {}
       query = event.content
       queries = query.split(' ', 1)
       print(queries[1])
       query_string = urllib.parse.urlencode({'search_query': queries[1]})
       print(query_string)
       html_content = urllib.request.urlopen('http://www.youtube.com/results?'+ query_string)
       print(html_content)
       search_content = html_content.read().decode()
       search_results = re.findall(r'\/watch\?v=([a-zA-Z0-9_-]{11})', search_content)
       print(search_results)
       await event.message.respond(f'{event.author.mention} looked up: https://youtube.com/watch?v=' + search_results[0])
  



@bot.command
@lightbulb.command('info', 'helper')
@lightbulb.implements(lightbulb.PrefixCommand)
async def helper(ctx):
    await ctx.respond('Commands: !info, !goodbye, !DM, !playing, !members, !multiply, !divide, !date, (.)youtube')
    
@bot.command
@lightbulb.command('date', 'todays date')
@lightbulb.implements(lightbulb.PrefixCommand)
async def date(ctx):
    await ctx.respond(f'The date is {today}')
    

    
@bot.command    
@lightbulb.command('goodbye', 'farewell')
@lightbulb.implements(lightbulb.PrefixCommand)
async def goodbye(ctx):
    await ctx.respond(f'Goodbye, {ctx.author.mention}..... :*(')
    
@bot.command    
@lightbulb.command('play', 'what game')
@lightbulb.implements(lightbulb.PrefixCommandGroup)
async def GameGroup(ctx):
    pass

@GameGroup.child
@lightbulb.command('monopoly', 'game 1')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    print(ctx)
    await ctx.respond(f'{ctx.author.mention} is playing monopoly')
    
@GameGroup.child
@lightbulb.command('scrabble', 'game 2')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond(f'{ctx.author.mention} is playing scrabble')
    
@bot.command
@lightbulb.option('num2', 'the second number', type=int)
@lightbulb.option('num1', 'the first number', type=int)
@lightbulb.command('multiply', 'Add two numbers together')
@lightbulb.implements(lightbulb.PrefixCommand)
async def multiply(ctx):
    numbersdict = []
    num1 = ctx.options.num1
    num2 = ctx.options.num2
    numbersdict = [num1, num2]
    print(numbersdict)
    await ctx.respond(f'Multiplying: {numbersdict} for {ctx.author.mention}')
    await ctx.respond(ctx.options.num1 * ctx.options.num2)
    
@bot.command
@lightbulb.option('num2', 'the second number', type=int)
@lightbulb.option('num1', 'the first number', type=int)
@lightbulb.command('divide', 'Add two numbers together')
@lightbulb.implements(lightbulb.PrefixCommand)
async def divide(ctx):
    numbersdict1 = []
    num1 = ctx.options.num1
    num2 = ctx.options.num2
    numbersdict1 = [num1, num2]
    print(numbersdict1)
    await ctx.respond(f'Dividing: {numbersdict1} for {ctx.author.mention}')
    await ctx.respond(ctx.options.num1 / ctx.options.num2)
    

    
    
    
bot.run()

