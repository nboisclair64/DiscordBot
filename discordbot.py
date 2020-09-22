import discord
from discord.ext import commands
from googlesearch import search
import asyncio
import json

client = commands.Bot(command_prefix='!')
client.remove_command("help")


@client.event
async def on_ready():
    print("The CovidBot is up and running!")
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server!')
    await channel.send("Welcome " + member + " to begin type !help")
@client.event
async def on_member_remove(member):
    print(f'{member} has left the server!')
    await channel.send("Goodbye " + member + "! Sorry to see you go :( ")



@client.command()
async def help(ctx):
    await ctx.send("To Begin type !Covid followed by one of the following keywords: \n -> Vaccine \n -> Prevention \n -> Breaking News \n -> Total Cases")

@client.command()
async def Covid(ctx,*,arg):
    if arg == str("Vaccine"):
        query = "Covid-19 vaccine progress"

        await ctx.send("The following article describes the most up-to-date info regarding the vaccine's progress: \n https://www.theguardian.com/world/ng-interactive/2020/jul/13/coronavirus-vaccine-tracker-how-close-are-we-to-a-vaccine")
    if arg == str("Prevention") :
        await ctx.send("To prevent COVID-19 do the following: \n 1.Wash Hands for 20 secounds \n 2.Wear a mask when in public \n 3. Maintain a social distance of 6ft")
    if arg == str("Breaking News"):
        query = "breaking news covid"
        for j in search (query, tld = "co.in", num=1,stop=1, pause=1 ):
            site = j
        await ctx.send("Here is the newest story regarding COVID-19 \n" + site)
    if arg == str("Total Cases"):
        await ctx.send("Please enter the name of the country you would like to see the Corona Virus statistics for following the original command.")
    if arg==str("Total Cases Canada"):
        query = "Total Cases of COVID-19 in Canada"
        for j in search (query, tld = "co.in", num=1,stop=1, pause=1 ):
            site = j

        await ctx.send("Click the link to take you to a live counter for COVID-19 Total Cases: \n" + site)    



client.run('IR_XyIs_YLFvVq_RkDQ5FM7GNsyskDdi')