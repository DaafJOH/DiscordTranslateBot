import discord, csv, re, io
from discord.ext import commands

filePath = '/home/doe040/Daaf/Vykeen/vykeen.txt'

try:
    file = open(filePath, "r")
    rip = file.read()
    file.close()
except FileNotFoundError:
    print("File not found. Please double check path.")
    exit()

def Translate(sentence):
    Tsentence = ""
    sentence = sentence.split(" ")
    for word in sentence:
        Tword = ""
        word = re.sub(r"\W|\d", "", word)
        word = word.lower()
        if (word != ""):
            if (re.search(r"\d+\s+"+word+r"\s+\w+\s+\w+", rip)):
                Tword = re.search(r"\s"+word+r"\s+\w+\s+\w+", rip)
                Tword = re.sub(r"\s\w+\s+\w+\s+", "", Tword.group())
                Tsentence = Tsentence + Tword + " "
            else:
                Tsentence = Tsentence + word + " "
    if (Tsentence != ""):
        return(Tsentence)
    else:
        return("Please enter a valid sentence to translate.")

def RTranslate(sentence):
    RTsentence = ""
    sentence = sentence.split(" ")
    for word in sentence:
        RTword = ""
        word = re.sub(r"\W|\d", "", word)
        word = word.lower()
        if (word != ""):
            if (re.search(r"\d+\s+\w+\s+\w+\s+"+word+"\s", rip, re.IGNORECASE)):
                RTword = re.search(r"\d+\s+\w+\s+\w+\s+"+word+"\s", rip, re.IGNORECASE)
                RTword = re.sub(r"\d+\s+|\s+\w+\s+\w+\s", "", RTword.group())
                RTsentence = RTsentence + RTword + " "
            elif (re.search(r"\d+\s+\w+\s+"+word+"\s", rip, re.IGNORECASE)):
                RTword = re.search(r"\d+\s+\w+\s+"+word+"\s", rip, re.IGNORECASE)
                RTword = re.sub(r"\d+\s+|\s+\w+\s", "", RTword.group())
                RTsentence = RTsentence + RTword + " "
            else:
                RTsentence = RTsentence + word + " "
    if (RTsentence != ""):
        return(RTsentence)
    else:
        return("Please enter a valid sentence to translate.")

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("Bot online")

@bot.command(aliases=['Grah!', 'grah', 'grah!'])
async def Grah(ctx, *, sentence):
    response = Translate(sentence)
    await ctx.send(response)

@bot.command(aliases=['Gruh?', 'gruh?', 'gruh'])
async def Gruh(ctx, *, sentence):
    response = RTranslate(sentence)
    await ctx.send(response)

bot.run("Bot token here")
