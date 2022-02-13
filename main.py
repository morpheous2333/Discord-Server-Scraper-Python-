
import discord
from discord import client
from discord import integrations
from discord.ext import commands
import os
import time
import requests
import asyncio
import colorama
from colorama import Fore
from colorama import init, Fore, Back, Style
colorama.init(autoreset=True)

os.system(f'cls & mode 85,20 & title [Specter] - Configuration')
token=input(Fore.CYAN+"Token:")


def check_token(token: str) -> str:
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": token}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token(token)

if token_type == "user":
    headers = {'Authorization': f'{token}'}
    client = commands.Bot(command_prefix='^',case_insensitive=False, self_bot=True,intents = discord.Intents.all())
else:
    headers = {'Authorization': f'Bot {token}'}
    client = commands.Bot(command_prefix='^',case_insensitive=False,intents = discord.Intents.all())
#I just gave it a prefix lol so I wouldn't get error
client.remove_command("help")


def clear():
    os.system("cls||clear")


def gui():
    os.system(f'cls & mode 85,20 & title [Specter Scraper] - Connected: {client.user}')
    print(Fore.LIGHTRED_EX+"""
       
        ███████╗██████╗ ███████╗ ██████╗████████╗███████╗██████╗ 
        ██╔════╝██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔══██╗
        ███████╗██████╔╝█████╗  ██║        ██║   █████╗  ██████╔╝
        ╚════██║██╔═══╝ ██╔══╝  ██║        ██║   ██╔══╝  ██╔══██╗
        ███████║██║     ███████╗╚██████╗   ██║   ███████╗██║  ██║  

        Scraper Developed by tb

        [1]-Scrape Info  

    """)


async def menu():
    os.system(f'cls & mode 85,20 & title [Specter Scraper] - Connected: {client.user}')

    while True:
        clear()
        gui()
        choice=input(Fore.CYAN+"Please Enter Your Choice:")
        if choice=="1":
            await scrape()
        else:
            print("Invalid Choice")
            
@client.event
async def on_ready():
    os.system('cls||clear')
    await menu()

async def scrape(): 
    

    global member_count
    global guild_id
    try:
        os.remove("members.txt")
        os.remove("channels.txt")
    except:
        pass

    member_count = 0
    guild_id = int(input('Enter Server ID: '))
    await client.wait_until_ready()
    ob = client.get_guild(guild_id)
    members = await ob.chunk()
    f= open('members.txt', 'a')
    for member in members:
        f.write(str(member.id) + "\n")
        member_count += 1

    channel_count=0
    channels=ob.channels
    x= open('channels.txt','a')
    for channel in channels:
        x.write(str(channel.id)+'\n')
        channel_count+=1
    
    role_count=0
    roles=ob.roles
    z=open('roles.txt','a')
    for role in roles:
        z.write(str(role.id)+'\n')
        role_count+=1
    print(Fore.LIGHTMAGENTA_EX+f"{member_count} Members")
    print(Fore.LIGHTMAGENTA_EX+f"{channel_count} Channels")
    print(Fore.LIGHTMAGENTA_EX+f"{role_count} Roles")


    time.sleep(2)
    


try:
    if token_type == "user":
        client.run(token, bot=False)
    elif token_type == "bot":
        client.run(token)
except:
    print(f'Invalid Token')
    time.sleep(2)
        
