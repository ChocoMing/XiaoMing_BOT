import discord
from discord.ext import commands, tasks
import asyncio
import time

bot = commands.Bot(
    Intents=discord.Intents.all(),
    command_prefix='<',
    description='一個很棒的機器人。')

prefix = "<"

@tasks.loop(seconds=1)
async def status_task():
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name=F"{prefix}指令"))
    await asyncio.sleep(5)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching, name="▌地震資訊"))
    await asyncio.sleep(5)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌編寫:巧克明#8831"))
    await asyncio.sleep(5)
    await bot.change_presence(status=discord.Status.idle,activity=discord.Activity(type=discord.ActivityType.watching,name="▌修改:ǝɹıɔ#0001"))
    await asyncio.sleep(5)

@bot.event
async def on_ready():
    status_task.start()
    print("啟動完畢！")
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    channel = bot.get_channel(805239007754977280)
    await channel.send(":white_check_mark: BOT啟動完畢")

@bot.command()
async def 公告(ctx, arg = None):
    if arg == "您沒有輸入內容":
        await ctx.send("請輸入公告內容")
    else:
        await ctx.message.delete()
        embed = discord.Embed(color=0xFF8800)
        embed.add_field(name=":loudspeaker: 公告",value=arg, inline=False)
        embed.set_footer(text=f"By.{ctx.message.author} ▌ 指令製作 猴子#3807", icon_url=f"{ctx.message.author.avatar_url}")
        await ctx.send(embed = embed)

@bot.command()
async def 狗腿(ctx):
    await ctx.send(f"<@{ctx.author.id}> 好帥對不對！！ 一定要說對歐！！！")
    await ctx.send("(並不是OwO)")

@bot.command()
async def 延遲(ctx):
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
@bot.event
async def on_message(message):
    if message.content == "喵":
        await message.channel.send(":cat2: 喵嗚~~~")

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
    embed=discord.Embed(title=":information_source: 指令", description="基本上沒有功能XD", color=0xff6600)
    embed.set_author(name="期待更新╰(*°▽°*)╯")
    embed.add_field(name="邀請連結", value="顯示我的邀請連結", inline=True)
    embed.add_field(name="我就爛", value="顯示梗圖", inline=True)
    embed.add_field(name="狗腿", value="你知道的...", inline=True)
    embed.add_field(name="放棄", value="呈現放棄狀態", inline=True)
    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")
    await ctx.send(embed=embed)

@bot.command()
async def 邀請連結(ctx):
    embed=discord.Embed(title="點我邀請BOT", url="https://discord.com/api/oauth2/authorize?client_id=828989412435034183&permissions=8&scope=bot", color=0xffa200)
    embed.set_footer(text=f"由 {ctx.author.name} 請求的資料", icon_url=f"{ctx.message.author.avatar_url}")
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    start = time.process_time()   
    await ctx.send(time.process_time() - start)

bot.run("TOKEN")