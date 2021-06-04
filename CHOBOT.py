import discord

from discord.ext import commands, tasks

import asyncio

import time

#SKIN
from json import loads
from requests import get
from base64 import b64decode

def jls_extract_def(Intents):
    return Intents


bot = commands.Bot(
    Intents=discord.Intents.all(),
    command_prefix='<',
    description='一個很棒的機器人。')


prefix = "<"

@tasks.loop(seconds=1)

async def status_task():

    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=F"▌{prefix}指令"))

    await asyncio.sleep(5)

    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="▌地震資訊"))

    await asyncio.sleep(5)

    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌編寫:巧克明#8831"))

    await asyncio.sleep(5)

    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌修改:ǝɹıɔ#0001"))

    await asyncio.sleep(5)

    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌指導:猴子#3807"))

    await asyncio.sleep(5)
    
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌我要睡覺啦QwQ"))

    await asyncio.sleep(5)


@bot.event

async def on_ready():

    status_task.start()

    print("啟動完畢！")

    print('Logged in as')

    print(bot.user.name)

    print(bot.user.id)

    print('------')

    #channel = bot.get_channel(805239007754977280)

    #await channel.send(":white_check_mark: BOT啟動完畢")


@bot.command()

async def 公告(ctx, arg = None):

    if arg == None:

        await ctx.send("請輸入公告內容")

    else:

        await ctx.message.delete()

        embed = discord.Embed(color=0xFF8800)

        embed.add_field(name=":loudspeaker: 公告",value=arg, inline=False)

        embed.set_footer(text=f"公告:{ctx.message.author}  ▌ 指令製作 猴子#3807", icon_url=f"{ctx.message.author.avatar_url}")

        await ctx.send(embed = embed)


@bot.command()

async def 狗腿(ctx):

    await ctx.send(f"<@{ctx.author.id}> 好帥對不對！！ 一定要說對歐！！！")

    await ctx.send("(~~並不是OwO~~)")


@bot.command()

async def 延遲(ctx):

    await ctx.message.delete()

    embed=discord.Embed(title="延遲", description="", color=0xff6600)

    embed.add_field(name="系統延遲", value="```我不會寫 教我```", inline=True)

    embed.add_field(name="API 延遲", value=f"```{int(bot.latency*1000)} (ms)```", inline=True)

    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)


@bot.command()

async def 經濟插件(ctx):

    await ctx.message.delete()

    embed=discord.Embed(title="MEE6經濟插件", description="", color=0xff6600)

    embed.add_field(name="!buy [名稱]", value="```從商店購買任何物品```", inline=True)

    embed.add_field(name="!daily", value="```領取您的每日硬幣。連續幾天要求獲得連勝獎金。```", inline=True)

    embed.add_field(name="!coins（可選成員）", value="```查詢服務器中任何人的硬幣數量```", inline=True)

    embed.add_field(name="!dice [金額]", value="```投擲兩個骰子，並嘗試獲得比對手更多的積分來獲得金幣```", inline=True)

    embed.add_field(name="!economy-info", value="```您需要了解的有關此服務器經濟性的所有信息```", inline=True)

    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)

#巧克伺服
@bot.command()

async def world(ctx):

    await ctx.message.delete()

    embed=discord.Embed(title="公告", description="", color=0xff6600)

    embed.add_field(name="伺服器已啟動" ,value="```剛剛服主在玩GTA```", inline=True)

    embed.set_footer(text=f"由 {ctx.author.name} 發布的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)


@bot.command()

async def 我就爛(ctx):

    embed=discord.Embed(title="我就爛!!!", color=0x2066d7)

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/828122882802581565/829333733416501248/Z.png")

    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)


@bot.command()

async def 放棄(ctx):

    await ctx.send(f"<@{ctx.author.id}>表示放棄")


#OAO


@bot.command()

async def TAG(ctx, *, arg):

    await ctx.message.delete()

    await ctx.send(f"<@{ctx.author.id}>還敢炸群阿!!! 冰鳥")


@bot.command()

async def A(ctx, *, arg):

    await ctx.message.delete()

    await ctx.send(f"<@{ctx.author.id}>還敢炸群阿!!! 冰鳥")


@bot.command()

async def say(ctx, *, arg):

    await ctx.message.delete()

    await ctx.send(arg)


@bot.command()

async def 指令(ctx):

    await ctx.message.delete()

    embed=discord.Embed(title=":information_source: 指令", description="基本上沒有功能XD", color=0xff6600)

    embed.set_author(name="慢慢製作中 ψ(｀∇´)ψ")

    embed.add_field(name="邀請機器人", value="顯示我的邀請連結", inline=True)

    embed.add_field(name="建立邀請", value="建立在這裡的邀請(永久)", inline=True)

    embed.add_field(name="我就爛", value="顯示梗圖", inline=True)

    embed.add_field(name="狗腿", value="你知道的...", inline=True)

    embed.add_field(name="放棄", value="呈現放棄狀態", inline=True)

    embed.set_footer(text=f"{ctx.author.name} 使用了 {prefix}指令", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)

@bot.command()

async def 邀請機器人(ctx):
    await ctx.message.delete()

    embed=discord.Embed(title="點我邀請BOT", url="https://discord.com/api/oauth2/authorize?client_id=828989412435034183&permissions=8&scope=bot", color=0xffa200)

    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)

#晚安
@bot.command()

async def 晚安(ctx):
    await ctx.message.delete()

    embed=discord.Embed(title=f"{ctx.author.name} 說晚安 :full_moon:", color=0xffa200)

    embed.set_footer(text="去睡覺啦！", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)

#清除訊息
@commands.command()
async def clean(self, ctx, num:int): 
    await ctx.channel.purge(limit=num+1)

@bot.command()

async def ping(ctx):

    start = time.process_time()   

    await ctx.send(time.process_time() - start)

@bot.command()

async def open(ctx):

    bot.get_channel("843454785663664158")
    await bot.edit_channel("伺服器已啟動")
    await ctx.send("已更改頻道標題")

@commands.command()
async def ytfds(ctx, channel):
    await get(ctx.guild.text_channel, name=channel).edit(name="XXX")

@bot.command()
async def t(self, ctx):
    channel = self.bot.get_channel(843454785663664158)
    await channel.edit(name="XXX")

#建立邀請連結 無美化
#@bot.command(pass_context=True)
#async def 建立邀請(ctx):
    #await ctx.message.delete()
    #invite = await ctx.channel.create_invite()
    #await ctx.send(invite.url)

@bot.command()

async def 建立邀請(ctx):
    await ctx.message.delete()
    invite = await ctx.channel.create_invite()
    embed=discord.Embed(title="邀請連結", url=invite.url, color=0xffa200)

    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")

    await ctx.send(embed=embed)

@bot.command()

async def 官方邀請(ctx):
    await ctx.message.delete()
    invite = await ctx.channel.create_invite()
    embed=discord.Embed(title="永久連結", url=invite.url, color=0xffa200)

    embed.set_footer(text=f"由 {ctx.author.name} 發布的資料", icon_url=f"{ctx.message.author.avatar_url}")
    embed.add_field(name="連結:", value=invite.url, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def skin(ctx, mcid:str):
    try:
        uuid = loads(get(url=f'https://api.mojang.com/users/profiles/minecraft/{mcid}').content.decode('UTF-8'))
    except:
        await ctx.send('ID 不存在')
    else:
        skinbase64 = loads(get(url=f'https://sessionserver.mojang.com/session/minecraft/profile/{uuid["id"]}').content.decode('UTF-8'))['properties'][0]['value']
        skin = eval(b64decode(skinbase64))
        await ctx.send(skin['textures']['SKIN']['url'])

@bot.command()

async def 簽到(ctx):
    await ctx.message.delete()
    invite = await ctx.channel.create_invite()
    embed=discord.Embed(title="簽到完成！",color=0xffa200)
    embed.set_footer(text=f"{ctx.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
    await ctx.send(embed=embed)

@bot.command()
async def potag(ctx):
    await ctx.message.delete()
# msg == bot發出來的訊息
    msg = await ctx.send('<@&838367423358566417>')
    await msg.message.delete()

bot.run("TONKEY")