import re
from discord.ext import commands

try: #import 'gek.txt' as GEK
    with open("gek.txt", "r") as file: GEK = file.read()
except FileNotFoundError:
    print("Could not find 'gek.txt' in given folder")
    exit()

try: #import 'korvax.txt' as KORVAX
    with open("korvax.txt", "r") as file: KORVAX = file.read()
except FileNotFoundError:
    print("Could not find 'korvax.txt' in given folder")
    exit()

try: #import 'vykeen.txt' as VYKEEN
    with open("vykeen.txt", "r") as file: VYKEEN = file.read()
except FileNotFoundError:
    print("Could not find 'vykeen.txt' in given folder")
    exit()

def Translate(language, sentence):
    Tsentence = ""
    sentenceList = sentence.split(" ")
    for word in sentenceList:
        Tword = ""
        word = re.sub(r"\W|\d", "", word).lower()
        if word != "":
            if re.search(r"\d+\s+"+word+r"\s+\w+\s+\w+", language):
                Tword = re.sub(r"\s\w+\s+\w+\s+", "", re.search(r"\s"+word+r"\s+\w+\s+\w+", language).group())
                Tsentence += Tword + " "
            else: Tsentence += word + " "
    if Tsentence != "": return(Tsentence)
    else: return("Please enter a valid sentence to translate.")

def Reverse_Translate(language, sentence):
    Tsentence = ""
    sentenceList = sentence.split(" ")
    for word in sentenceList:
        Tword = ""
        word = re.sub(r"\W|\d", "", word).lower()
        if word != "":
            if re.search(r"\d+\s+\w+\s+\w+\s+"+word+"\s", language, re.IGNORECASE):
                Tword = re.sub(r"\d+\s+|\s+\w+\s+\w+\s", "", re.search(r"\d+\s+\w+\s+\w+\s+"+word+"\s", language, re.IGNORECASE).group())
                Tsentence += Tword + " "
            elif re.search(r"\d+\s+\w+\s+"+word+"\s", language, re.IGNORECASE):
                Tword = re.sub(r"\d+\s+|\s+\w+\s", "", re.search(r"\d+\s+\w+\s+"+word+"\s", language, re.IGNORECASE).group())
                Tsentence += Tword + " "
            else: Tsentence += word + " "
    if Tsentence != "": return(Tsentence)
    else: return("Please enter a valid sentence to translate.")

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("Bot online")


@bot.command(aliases=['gek'])
async def Gek(ctx, *, sentence):
    await ctx.send(Translate(GEK, sentence))

@bot.command(aliases=['korvax'])
async def Korvax(ctx, *, sentence):
    await ctx.send(Translate(KORVAX, sentence))

@bot.command(aliases=['vykeen', 'grah', 'Grah'])
async def Vykeen(ctx, *, sentence):
    await ctx.send(Translate(VYKEEN, sentence))


@bot.command(aliases=['gektoenglish'])
async def GekToEnglish(ctx, *, sentence):
    await ctx.send(Reverse_Translate(GEK, sentence))

@bot.command(aliases=['korvaxtoenglish'])
async def KorvaxToEnglish(ctx, *, sentence):
    await ctx.send(Reverse_Translate(KORVAX, sentence))

@bot.command(aliases=['vykeentoenglish', 'gruh', 'Gruh'])
async def VykeenToEnglish(ctx, *, sentence):
    await ctx.send(Reverse_Translate(VYKEEN, sentence))


bot.run("Bot token here")