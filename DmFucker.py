try:
    import os, time, threading, colorama, discord, random
    from colorama import Fore, Back, Style
    from discord.ext import commands

except:
    import os, time
    os.system("pip install threading")
    os.system("pip install colorama")
    os.system("pip install discord")
    import os, time, threading, colorama, discord, random
    from colorama import Fore, Back, Style
    from discord.ext import commands

os.system("title MassDm - By ReyZ")
print(Fore.CYAN + "type Help to get Info about this Tool.")
print("")
InvalidTokens = []
dmspamthreadhandler = 0
def dmspam():
    import time
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())

    @bot.event
    async def on_ready():
        print("Bot is Working and total Functional! :D")
        await bot.user.edit(username=nickofbots)
        await bot.change_presence(status=discord.Status.offline, activity=discord.Activity(type=discord.ActivityType.playing, name="HEIL SVF"))


    @bot.command()

    async def dm(ctx, times=None, user_id=None, *, args=None):
        if times != None and user_id != None:
            if args != None:
                if ctx.author.id == int(userid):
                    try:
                        target = await bot.fetch_user(user_id)
                        await ctx.channel.send("'" + args + "' Is getting send to: " + target.name)
                        for i in range(int(times)):
                            time.sleep(0.5)
                            try:
                                await target.send(args)
                                print(Fore.LIGHTCYAN_EX + "[+] " + Fore.CYAN + "Sent Message.")
                            except:
                                print(Fore.YELLOW + "[/] Rate Limit: Handler Waiting 2 seconds.")
                                time.sleep(2)

                    except:
                        pass
                        print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "Failed To Send Message.")
            else:
                fuckembed = discord.Embed(title="𝓕𝓤𝓒𝓚𝓔𝓓 𝓑𝓨 𝓢𝓥𝓕", description="ĦɆƗŁ SVF", colour=discord.Colour.red())
                fuckembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1049714006673338379/1103018713990574210/SVFlogo.png")
                fuckembed.add_field(name="WHAT IS SVF?", value="SVF IS AN DISCORD SERVER/ACCOUNT NUKING GROUP", inline=False)
                fuckembed.add_field(name="GG, PRAISE SVF", value="𝕋ℍ𝕀𝕊 𝔸ℂℂ𝕆𝕌ℕ𝕋 𝔾𝕆𝕋 𝔽𝕌ℂ𝕂𝔼𝔻 𝔹𝕐 𝕊𝕍𝔽", inline=False)
                fuckembed.add_field(name="𝒟𝐼𝒮𝒞𝒪𝑅𝒟", value="https://discord.gg/TU8F8tYThA", inline=False)
                fuckembed.add_field(name="𝒴𝒪𝒰𝒯𝒰𝐵𝐸", value="https://www.youtube.com/@reyz7422 & https://www.youtube.com/@Dummergoki", inline=False)
                if ctx.author.id == int(userid):
                    try:
                        target = await bot.fetch_user(user_id)
                        await ctx.channel.send("The Embed is getting send to: " + target.name)
                        for i in range(int(times)):
                            time.sleep(0.5)
                            try:
                                await target.send(embed=fuckembed)
                                print(Fore.LIGHTCYAN_EX + "[+] " + Fore.CYAN + "Sent Message.")
                            except:
                                print(Fore.YELLOW + "[/] Rate Limit: Handler Waiting 2 seconds.")
                                time.sleep(2)
                    except:
                        pass
                        print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "Failed To Send Message.")

        else:
            print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "A user_id and/or times were not included.")
    
    @bot.command()
    async def stop(ctx):
        if ctx.author.id == int(userid):
            print(Fore.LIGHTRED_EX + "[-] " + Fore.RED + "Exited Bot.")
            exit()

    bot.run(dmtoken)

def cttest():
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

    @bot.event
    async def on_ready():
        channel = bot.get_channel(int(askForChannelIDCT))
        try:
            await channel.send("Message Sent.")
        except:
            print(Fore.RED + "Failed with token " + cttoken + Fore.CYAN)
            InvalidTokens.append(cttoken)
    try:        
        bot.run(cttoken)
    except:
        print(Fore.RED + "Failed with token " + cttoken + Fore.CYAN)
        InvalidTokens.append(cttoken)

while True:
    cmd = input(Fore.GREEN + "$ Input $ : " + Fore.MAGENTA)

    if cmd == "Help" or cmd == "help":
        print(Fore.CYAN + r"""
This is an Discord MassDM Tool Coded by ReyZ, Here are the Commands:

SetID [SI] - sets your user id so you are the only one that can spam.
CheckTokens [CT] - Checks if the tokens in the Tokens.txt are Real.
StartBots [SB] - Starts the bots.
        """)

    if cmd == "SI" or cmd == "si" or cmd == "sI" or cmd == "Si":
        keyword = input(Fore.CYAN + "USERID: " + Fore.MAGENTA)
        time.sleep(0.5)
        print(Fore.CYAN + "Setting UserID...")
        with open("user_id.txt", "w") as keyfile:
            keyfile.write(keyword)
            time.sleep(1)
            print(Fore.CYAN + "UserID Set!")

    if cmd == "CT" or cmd == "ct" or cmd == "cT" or cmd == "Ct":
        askiftokensinserver = input(Fore.CYAN + "[REMINDER] Did you get all bots into the server?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askiftokensinserver == "n" or askiftokensinserver == "N":
            pass
        if askiftokensinserver == "y" or askiftokensinserver == "Y":
            askForChannelIDCT = input(Fore.CYAN + "all bots need to write an test message into a server, ChannelID: " + Fore.MAGENTA)
            print(Fore.CYAN + "Checking all Lines...")
            file1 = open('tokens.txt', 'r')
            Lines = file1.readlines()
            print(Fore.CYAN + "Checked all Lines.")
            time.sleep(0.5)

            for line in Lines:
                cttoken = line
                time.sleep(0.1)
                ctthread = threading.Thread(target=cttest)
                ctthread.start()
            
            time.sleep(10)
            print(Fore.LIGHTRED_EX + "INVALID TOKENS: \n" + Fore.RED)
            print(*InvalidTokens, sep = "\n")
            askifcleartokens = input(Fore.CYAN + "Delete Invalid Tokens?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)

            if askifcleartokens == "Y" or askifcleartokens == "y":

                with open("tokens.txt", "r") as file:
                    lines = file.readlines()
                with open("tokens.txt", "w") as file:
                    for line in lines:
                        if not any(word in line for word in InvalidTokens):
                            file.write(line)

                print(Fore.CYAN + "Finished.")

            if askifcleartokens == "N" or askifcleartokens == "n":
                pass

    if cmd == "SB" or cmd == "sb" or cmd == "sB" or cmd == "Sb":
        prefix = input(Fore.CYAN + "Prefix: " + Fore.MAGENTA)
        askifchangenick = input(Fore.CYAN + "Change name of all Bots?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askifchangenick == "Y" or askifchangenick == "y":
            nickofbots = input(Fore.CYAN + "Name: " + Fore.MAGENTA)

        file1 = open('tokens.txt', 'r')
        Lines = file1.readlines()
        
        with open("user_id.txt", "r") as readuserid:
            userid = readuserid.readline()

        for line in Lines:
            print(Fore.CYAN)
            dmspamthreadhandler = dmspamthreadhandler + 1
            dmtoken = line
            dmthread = threading.Thread(target=dmspam)
            dmthread.start()
            if dmspamthreadhandler == 5:
                print(Fore.YELLOW + "[/] " + Fore.YELLOW + "Thread Handler waiting 0.5 seconds." + Fore.CYAN)
                time.sleep(0.5)
                dmspamthreadhandler = 0