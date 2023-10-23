import os
import discord
import pymongo
from discord import app_commands
import asyncio
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from discord.ext import commands
username=os.environ['username']
password = os.environ['Password']
uri = f"mongodb+srv://{username}:{password}@wecbot.ra9zx6y.mongodb.net/?retryWrites=true&w=majority"
# Define the bot prefix
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
mongodb_client=pymongo.MongoClient(uri)
db=mongodb_client['WEC_Discord_Bot_DataBase']
@bot.command(aliases=['Hello','Hey','HELLO'])
async def hello(ctx):
    await ctx.send('Hello!!')
@bot.command(aliases=['SIGs', 'sigs'])
async def list_sigs(ctx):
    collection = db['SIGs']
    sig_data = collection.find()
    response = "SIGs:\n\n"
    for sig in sig_data:
        response += f"{sig['name']} \n {sig['description']}\n\n"
    await ctx.send(response)
@bot.command(aliases=['pastevents','pevents','past events'])
async def past_events(ctx):
 collection = db['PAST_EVENTs']
 past_events_data = collection.find()
 response = "PAST EVENTS:\n"
 for event in past_events_data:
    event_info = f"{event['name']}\n{event['date']} \n {event['time']}\n {event['venue']}\n {event['description']}\n"
    # Check if adding the event_info will exceed the character limit
    if len(response) + len(event_info) > 2000:
        await ctx.send(response)  
        response = "" 
    response += event_info
 if response:
    await ctx.send(response)

@bot.command(aliases=['upcomingevents' , 'uevents',"upcoming events"])
async def upcoming_events(ctx):
 collection = db['UPCOMING_EVENTs']
 upcoming_events_data = collection.find()
 response = "UPCOMING EVENTS:\n"
 for event in upcoming_events_data:
    event_info = f"{event['name']}\n{event['date']}\n{event['time']}\n {event['venue']}\n {event['description']}\n"
    # Check if adding the event_info will exceed the character limit
    if len(response) + len(event_info) > 2000:
        await ctx.send(response)  
        response = "" 
    response += event_info
 if response:
    await ctx.send(response) 
@bot.command(aliases=['core','TEAM'])
async def team(ctx):
 collection = db['TEAM']
 team_members = collection.find()
 response = "TEAM MEMBERS:\n"
 for member in team_members:
   team_info = f"{member['name']} \n {member['position']} \n {member['github']}\n {member['gmail']}\n {member['linkedin']}\n"
   if len(response) + len(team_info) > 2000:
     await ctx.send(response)  # Send the current response
     response = ""  # Reset the response

   response += team_info
 if response:
    await ctx.send(response) 

try:
  token = os.getenv("TOKEN") or ""
  if token == "":
    raise Exception("Please add your token to the Secrets pane.")
  bot.run(token)
except discord.HTTPException as e:
    if e.status == 429:
        print(
            "The Discord servers denied the connection for making too many requests"
        )
        print(
            "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
        )
    else:
        raise e
