import discord
import random
import os
from lists import codes
from discord import Embed
from discord.ext import commands

token = open("token.txt", "r").readline()
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='$')


@bot.event
async def on_ready():
    print('we have logged in as {0.user}'.format(bot))


@bot.command()
async def bonk(ctx):
    await ctx.channel.send(
        'horny people have no rights. horny people are NOT protected under the constitution. if you are horny i WILL'
        ' find you and then you will be sorry buster. unfollow me right fucking now if you are horny, have ever been'
        ' horny, or ever will be horny. this is not a joke. please leave.')


@bot.command()
async def sins(ctx):
    path = random.choice(os.listdir('E:/Pictures/sins/'))
    await ctx.channel.send(file=discord.File("E:/Pictures/sins/" + path))


@bot.command()
async def nsfw(ctx):
    path = random.choice(os.listdir('D:/cache/cache/'))
    print(path)
    if isinstance(ctx.channel, discord.channel.DMChannel) is True or ctx.channel.is_nsfw() is True:
        await ctx.channel.send(f"http://69.136.183.114/cache/cache/{path}")
    else:
        await ctx.channel.send('Use this command in an nsfw channel my guy')


@bot.command()
async def commands(ctx):
    embedvar: Embed = discord.Embed(title="Available commands:", color=0xFF5733)
    embedvar.add_field(name='bonk', value='sends anti-horny copypasta', inline=False)
    embedvar.add_field(name='sins', value="sends an image from my sins folder (sfw)", inline=False)
    embedvar.add_field(name="nsfw",
                       value="sends an image from the special folder (nsfw) - only useable in nsfw channels due to "
                             "complaints",
                       inline=False)
    embedvar.add_field(name="message",
                       value='format as [userid "content to send"] please. If ur message is multiple words, put them'
                             ' all in quotations.',
                       inline=False)
    embedvar.add_field(name='launchcodes',
                       value='selects a "special" code provided by @K-01#9545 - also only useable in nsfw channels')
    await ctx.channel.send(embed=embedvar)


@bot.command()
async def message(ctx, target: discord.User, message):
    try:
        if target.dm_channel is None:
            await target.create_dm()
        await target.dm_channel.send(message)
        await ctx.channel.send('message sent!')
    except:
        await ctx.channel.send("messaged failed to deliver")


@bot.command()
async def launchcodes(ctx):
    x = random.choice(codes)
    if isinstance(ctx.channel, discord.channel.DMChannel) is True or ctx.channel.is_nsfw() is True:
        await ctx.channel.send(f'https://nhentai.net/g/{x}')
    else:
        await ctx.channel.send(x)


@bot.command()
async def cum(ctx):
    await ctx.channel.send("Infinite cum. You sit on the toilet to jack off, but you begin to cum uncontrollably. "
                           "After ten spurts you start to worry. Your hand is sticky and it reeks of semen. You "
                           "desperately shove your dick into a wad of toilet paper, but that only makes your balls "
                           "hurt. The cum accelerates. It’s been three minutes. You can’t stop cumming. Your bathroom "
                           "floor is covered in a thin layer of baby fluid. You try to cum into the shower drain but "
                           "it builds up too fast. You try the toilet. The cum is too thick to be flushed. You lock "
                           "the bathroom door to prevent the cum from escaping. The air grows hot and humid from the "
                           "cum. The cum accelerates. You slip and fall in your own sperm. The cum is now six inches "
                           "deep, almost as long as your still-erect semen hose. Sprawled on your back, you begin to "
                           "cum all over the ceiling. Globs of the sticky white fluid begin to fall like raindrops, "
                           "giving you a facial with your own cum. The cum accelerates. You struggle to stand as the "
                           "force of the cum begins to propel you backwards as if you were on a bukkake themed "
                           "slip-and-slide. Still on your knees, the cum is now at chin height. To avoid drowning you "
                           "open the bathroom door. The deluge of man juice reminds you of the Great Molasses Flood "
                           "of 1919, only with cum instead of molasses. The cum accelerates. It’s been two hours. "
                           "Your children and wife scream in terror as their bodies are engulfed by the snow-white "
                           "sludge. Your youngest child goes under, with viscous bubbles and muffled cries rising "
                           "from the goop. You plead to God to end your suffering.")
    await ctx.channel.send("The cum accelerates. You squeeze your dick to stop the cum, but it begins to leak out of "
                           "your asshole instead. You let go. The force of the cum tears your urethra open, "
                           "leaving only a gaping hole in your crotch that spews semen. Your body picks up speed as "
                           "it slides backwards along the cum. You smash through the wall, hurtling into the sky at "
                           "thirty miles an hour. From a bird’s eye view you see your house is completely white. "
                           "Your neighbor calls the cops. The cum accelerates. As you continue to ascend, "
                           "you spot police cars racing towards your house. The cops pull out their guns and take "
                           "aim, but stray loads of cum hit them in the eyes, blinding them. The cum accelerates. "
                           "You are now at an altitude of 1000 feet. The SWAT team arrives. Military helicopters "
                           "circle you. Hundreds of bullets pierce your body at once, yet you stay conscious. Your "
                           "testicles have now grown into a substitute brain. The cum accelerates. It has been two "
                           "days. With your body now destroyed, the cum begins to spray in all directions. You break "
                           "the sound barrier. The government deploys fighter jets to chase you down, but the impact "
                           "of your cum sends one plane crashing to the ground. The government decides to let you "
                           "leave the earth. You feel your gonads start to burn up as you reach the edges of the "
                           "atmosphere. You narrowly miss the ISS, giving it a new white paint job as you fly past. "
                           "Physicists struggle to calculate your erratic trajectory. The cum accelerates. The cum "
                           "begins to gravitate towards itself, forming a comet trail of semen. Astronomers begin "
                           "calling you the “Cummet.” You are stuck in space forever, stripped of your body and "
                           "senses, forced to endure an eternity of cumshots. Eventually, you stop thinking.")


@bot.command()
async def stallman(ctx):
    await ctx.channel.send("I’d just like to interject for a moment. What you’re refering to as Linux, is in fact, "
                           "GNU/Linux, or as I’ve recently taken to calling it, GNU plus Linux. Linux is not an "
                           "operating system unto itself, but rather another free component of a fully functioning "
                           "GNU system made useful by the GNU corelibs, shell utilities and vital system components "
                           "comprising a full OS as defined by POSIX. "
                           "\nMany computer users run a modified version of the GNU system every day, without realizing"
                           " it. Through a peculiar turn of events, the version of GNU which is widely used today is "
                           "often called Linux, and many of its users are not aware that it is basically the GNU "
                           "system, developed by the GNU Project. "
                           "\nThere really is a Linux, and these people are using it, but it is just a part of the "
                           "system they use. Linux is the kernel: the program in the system that allocates the "
                           "machine’s resources to the other programs that you run. The kernel is an essential part "
                           "of an operating system, but useless by itself; it can only function in the context of a "
                           "complete operating system. Linux is normally used in combination with the GNU operating "
                           "system: the whole system is basically GNU with Linux added, or GNU/Linux. All the "
                           "so-called Linux distributions are really distributions of GNU/Linux!")


bot.run(token)