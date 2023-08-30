try:
    import os, time, threading, colorama, discord, random, requests
    from colorama import Fore, Back, Style
    from discord.ext import commands

except:
    import os, time
    print("Failed To Import The Packages, Installing The Requirements.txt.")
    time.sleep(2)
    os.system("pip install -r requirements.txt")
    import os, time, threading, colorama, discord, random, requests
    from colorama import Fore, Back, Style
    from discord.ext import commands
    print("Sucessfully Installed And Imported the Packages!")
    time.sleep(2)
    os.system("cls")

os.system("title MassDm - By ReyZ")

with open('tokens.txt') as tokens:
    totaltokens = sum(1 for line in tokens)

print(Fore.BLUE + "You Got " + Fore.CYAN + str(totaltokens) + Fore.BLUE + " Bot Tokens.")

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
    
        if nickofbots is not None:
            await bot.user.edit(username=nickofbots)
    
        await bot.change_presence(status=discord.Status.offline, activity=discord.Activity(type=discord.ActivityType.playing, name="HEIL SVF"))
    
        if idofuser is None or times is None:
            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + "-" +  Fore.WHITE + "] " + Fore.RED + "A user_id and/or times were not included.")
            return
    
        aws = 0
        try:
            target = await bot.fetch_user(idofuser)
        
            if message is not None:
            
                for i in range(int(times)):
                    time.sleep(random.uniform(0.02, 0.3))
                
                    try:
                        await target.send(message)
                        aws += 1
                        print(Fore.WHITE + "[" + Fore.CYAN + "+" +  Fore.WHITE + "] " + Fore.CYAN + f"Sent Message. Messages That Were Sent > {str(aws)}.")
                    except discord.errors.HTTPException:
                        print(Fore.WHITE + "[" + Fore.YELLOW + "/" +  Fore.WHITE + "] " + Fore.YELLOW + "Rate Limit: Handler Waiting 2 seconds.")
                        time.sleep(2)
        
            else:
                fuckembed = discord.Embed(title="FUCKED BY SVF", description="ĦɆƗŁ SVF", colour=discord.Colour.red())
                fuckembed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1049714006673338379/1103018713990574210/SVFlogo.png")
                fuckembed.add_field(name="WHAT IS SVF?", value="SVF IS A DISCORD SERVER/ACCOUNT NUKING GROUP​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​   ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​   ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​   ", inline=False)
                fuckembed.add_field(name="GG, PRAISE SVF", value="𝕋ℍ𝕀𝕊 𝔸ℂℂ𝕆𝕌ℕ𝕋 𝔾𝕆𝕋 𝔽𝕌ℂ𝕂𝔼𝔻 𝔹𝕐 𝕊𝕍𝔽", inline=False)
                fuckembed.add_field(name="𝒟𝐼𝒮𝒞𝒪𝑅𝒟", value="https://discord.gg/CSK83jfBC8", inline=False)
                fuckembed.add_field(name="𝒴𝒪𝒰𝒯𝒰𝐵𝐸", value="https://www.youtube.com/@0reyz & https://www.youtube.com/@Dummergoki", inline=False)
                fuckembed.set_footer(text="This DM Spammer is a Open Source Project made by ReyZ, github: https://github.com/ReyZ0309/ | Praise SVF")
                target = await bot.fetch_user(idofuser)
                
                for i in range(int(times)):
                    time.sleep(random.uniform(0.02, 0.3))
                    
                    try:
                        await target.send(embed=fuckembed)
                        aws += 1
                        print(Fore.WHITE + "[" + Fore.CYAN + "+" +  Fore.WHITE + "] " + Fore.CYAN + f"Sent Message. Messages That Were Sent > {str(aws)}.")
                    except discord.errors.HTTPException:
                        print(Fore.WHITE + "[" + Fore.YELLOW + "/" +  Fore.WHITE + "] " + Fore.YELLOW + "Rate Limit: Handler Waiting 2 seconds.")
                        time.sleep(2)
            
        except discord.errors.NotFound:
            print(Fore.WHITE + "[" + Fore.MAGENTA + "-" +  Fore.WHITE + "] " + Fore.MAGENTA + "Failed to find the target user.")
    
    @bot.command()
    async def stop(ctx):
        if ctx.author.id == int(userid):
            print(Fore.WHITE + "[" + Fore.LIGHTRED_EX + "-" +  Fore.WHITE + "] " + Fore.RED + "Exited Bot.")
            exit()

    bot.run(dmtoken)

InvalidTokens = []

def create_cttest(cttoken):
    def cttest():
        import requests
        from colorama import Fore
        token = cttoken.strip()
        header = {"Authorization": f"Bot {token}"}
        toggle = True

        while toggle is True:
            r = requests.get("https://discord.com/api/v9/users/@me", headers=header)
            
            if r.status_code == 200:
                print(Fore.WHITE + "[" + Fore.CYAN + "+" +  Fore.WHITE + "] " + Fore.CYAN + "Valid Token.")
                toggle = False

            elif r.status_code == 429:
                print(Fore.WHITE + "[" + Fore.YELLOW + "/" +  Fore.WHITE + "] " + Fore.YELLOW + "Ratelimit.")
                time.sleep(0.69)
            
            else:
                print(Fore.WHITE + "[" + Fore.MAGENTA + "-" +  Fore.WHITE + "] " + Fore.MAGENTA + "Invalid Token.")
                InvalidTokens.append(token)
                toggle = False

    return cttest

while True:
    cmd = input(Fore.GREEN + "$ Input $ : " + Fore.MAGENTA)

    if cmd == "Help" or cmd == "help":
        print(Fore.CYAN + r"""
This is an Discord MassDM Tool Coded by ReyZ, Here are the Commands:

CheckTokens [CT]
MassDM [MD]
        """)

    if cmd == "CT" or cmd == "ct" or cmd == "cT" or cmd == "Ct":
        file1 = open('tokens.txt', 'r')
        Lines = file1.readlines()
        time.sleep(0.5)

        for line in Lines:
            cttoken = line
            running = 1
            time.sleep(0.1)
            ctthread = threading.Thread(target=create_cttest(cttoken))
            ctthread.start()
            
        time.sleep(5)
        print(Fore.LIGHTRED_EX + "INVALID TOKENS: \n" + Fore.RED)
        print(*InvalidTokens, sep = "\n")
        print("")
        print(Fore.CYAN + "if no tokens are shown all your tokens are valid")
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

    if cmd == "MD" or cmd == "md" or cmd == "mD" or cmd == "Md":
        runned = 0
        prefix = input(Fore.CYAN + "Prefix: " + Fore.MAGENTA)
        askifchangenick = input(Fore.CYAN + "Change name of all Bots?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA)
        if askifchangenick == "Y" or askifchangenick == "y":
            nickofbots = input(Fore.CYAN + "Name: " + Fore.MAGENTA)
        else:
            nickofbots = None
        
        idofuser = input(Fore.CYAN + "ID of the person you want to DM: " + Fore.MAGENTA)
        times = input(Fore.CYAN + "How Much DMs to send to the user per bot: " + Fore.MAGENTA)
        blah = input(Fore.CYAN + "Use Custom Message?" + Fore.MAGENTA + " y/n" + Fore.CYAN + " : " + Fore.MAGENTA + Fore.MAGENTA)
        if blah == "y":
            message = input(Fore.CYAN + "Message To Send: " + Fore.MAGENTA)
        else:
            message = None

        file1 = open('tokens.txt', 'r')
        Lines = file1.readlines()
        

        for line in Lines:
            print(Fore.CYAN)
            dmtoken = line
            dmthread = threading.Thread(target=dmspam)
            dmthread.start()
    
