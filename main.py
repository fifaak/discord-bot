#ลิขสิทธิ์ source code โดย fifaak
#comment ภาษาไทย

#module ที่เรียกใช้
from datetime import datetime, timedelta
from click import pass_context
from discord.utils import get
from discord import FFmpegPCMAudio
from gtts import gTTS
import os
from mutagen.mp3 import MP3
from youtube_dl import YoutubeDL
import time
import discord
from discord.ext import commands
import asyncio
times = datetime.now()
bot = commands.Bot(command_prefix="!",help_command=None)
def audio_len(path):
    global MP3
    audio = MP3(path)
    return(audio. info.length)



@bot.event 
async def on_ready():
    print(f"บอท {bot.user} เข้ามาแล้ว")
    await bot.change_presence(activity=discord.Activity(name="ห้องสอบ", type=5)) #โชว์ status




@bot.event #ตอบรับการสวัสดี
async def on_message(message):
    msg_content = message.content.lower()
    hi_word = ['hi','hello','สวัสดี','หวัดดี']
    if message.author.id == bot.user.id or message.author.id == (id ที่ต้องการละเว้น):
        return
    elif any(hiword in msg_content for hiword in hi_word):
        await message.channel.send("หวัดดรีครุบพี่"+str(message.author.name))
    await bot.process_commands(message)



@bot.command() #เช็คยศต่างๆใน server (ต้องตั้งค่าเพิ่มใน DISCORD DEVELOPER PORTAL)
async def roles(ctx):
    c = 0
    list = (" \n".join([(str(c:=c+1))+".) "+str(r)+" ( "+str(len(r.members))+" คน  )" for r in ctx.guild.roles]))
    emBed = discord.Embed(title="ข้อมูลพื้นฐาน" ,color=0x42f5a7,description=f"***ตำแหน่งต่างๆ***\n"+list.replace("@",""))
    emBed.add_field(name="เช็คล่าสุด",value=times)
    await ctx.send(embed=emBed)


@bot.command() #ส่ง embed รายละเอียดพื้นฐานของบอท
async def งง(ctx):
    emBed = discord.Embed(title="401's bot" ,color=0x42f5a7)
    emBed.set_image(url="https://s.isanook.com/ns/0/rp/rc/w850h510/yatxacm1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL25zLzAvdWQvMTY1LzgyNjM0NS9saW5nLmpwZw==.jpg")
    emBed.add_field(name="เกี่ยวกับบอท", value="เวอร์ชั่น: 1.0\nเขียนโดย: fifa.js\nเขียนด้วยภาษา: Python\nส่วนเสริม:\n-datetime     -ffmpeg\n-gtts      -os\n-youtube_dl        -time\n-discord     -asyncio\n-mutagen.mp3", inline=False)
    emBed.add_field(name="คำสั่งนำหน้า", value="ใช้เป็นเครื่องหมาย !", inline=False)
    emBed.add_field(name="!เล่น + url", value="เล่นเพลงตามด้วยลิ้ง", inline=False)
    emBed.add_field(name="!c", value="คิดเลขผ่านดิส", inline=False)
    emBed.add_field(name="!ออก", value="ออกจากช่องเสียง", inline=False)
    emBed.add_field(name="!ปิดระบบ", value="หยุดระบบทุกอย่าง", inline=False)
    emBed.add_field(name="!spam + เลข", value="สแปมเข้าออกรัวๆ (ใช้พอเป็นพิธี)", inline=False)
    emBed.add_field(name="!พูด + ประโยค", value="บอทจะเข้ามาพูดตามที่พิมพ์", inline=False)
    emBed.add_field(name="อื่นๆ", value="ฟังก์ชั่นหาทำที่ต้องค้นหากันเอาเอง", inline=False)
    emBed.set_footer(text='คริๆ', icon_url='https://png.vector.me/files/images/3/8/384579/warning_icon_preview')
    await ctx.channel.send(embed = emBed)

@bot.command() #ฟังก์ชั่นช่วยคิดเลข
async def c(ctx, operation:str):
    caled = eval(operation)
    await ctx.send("= "+str('{:.5f}'.format(caled)))
#นิวเคลียร์
@bot.command(pass_context = True)
async def ww2(ctx):
    print("Choose the server: A B")
    server = str(input("Choose the server: "))
    if server == "C":
        def oxx(eventt):
            if eventt == 1:
                print("C <---selected")
                print("ชื่อช่องเสียง 1 = a")
                print("ชื่อช่องเสียง 2 = b")
                place_t = str(input("ID: "))
                if place_t == "a":
                    channel_id = ไอดีช่องเสียง1
                if place_t == "b":
                    channel_id = ไอดีช่องเสียง2
                    return channel_id
            else:
                pass
            return channel_id
        channel_id = oxx(1)
    elif server == "B":
        def ids(event):
            if event == 1:
                print("303 <---selected")
                print("---- Choose the voice channel ----")
                print("ชื่อช่องเสียง 1 = a")
                print("ชื่อช่องเสียง 2 = b")
                place_ox = str(input("ID: "))
                if place_ox == "a":
                    channel_id = ไอดีช่องเสียง1
                if place_ox == "b":
                    channel_id = ไอดีช่องเสียง2
                    return channel_id
                else:
                    print("Wrong!!!")
            else:
                pass
            return channel_id
        channel_id = ids(1)

    print("----WW2 choose some voice: yourvoice1 yourvoice2----")
    print(channel_id)
    voice_channel = bot.get_channel(channel_id)
    nuclear = str(input("Which nuclear: "))
    if nuclear == "yourvoice1":
        
        channel = None
        if voice_channel != None:
            channel = voice_channel
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=r"your audiofile path"))
            while vc.is_playing():
                time.sleep(.1)
            time.sleep(3)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "ใช้ฟังก์ชั่นไม่ได้")
        
        await ctx.message.delete()
        print("finished")
    elif nuclear == "yourvoice2":
        channel = None
        if voice_channel != None:
            channel = voice_channel
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source=r"your audiofile path"))
            while vc.is_playing():
                time.sleep(.1)
            time.sleep(3)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "ใช้ฟังก์ชั่นไม่ได้")
        
        await ctx.message.delete()
        print("ระเบิดแล้ว")
  

@bot.command(pass_context=True) #พูดตามสิ่งที่พิมพ์โดยบอทจะเข้ามาในช่องที่ผู้พิมพ์อยู่ (voice channel)
async def พูด(ctx,*,text):
    voice_channel = ctx.author.voice.channel
    global gTTS
    speech = gTTS (text = text,lang="th" , slow = True)
    speech.save("audio.mp3")
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio("audio.mp3"), after=lambda e: print("เสร็จละ"))
    counter = 0
    cwd = os.getcwd()
    duration = audio_len(cwd + "/audio.mp3")
    while not counter >= duration:
        time.sleep(2)
        counter += 1
    await vc.disconnect()



@bot.command(pass_context=True) #tts ตามที่พิมพ์โดยพิมพ์ผ่าน terminal
async def tts(ctx):
    print("Choose the server: เทสบอท 303 401")
    server = str(input("Choose the server: "))
    if server == "เทสบอท":
        def oxx(eventt):
            if eventt == 1:
                print("เทสบอท <---selected")
                print("ทัวไป = a")
                place_t = str(input("ID: "))
                if place_t == "a":
                    channel_id = ไอดีช่อง
                    return channel_id
            else:
                pass
            return channel_id
        channel_id = oxx(1)

    text = str(input("พิมพ์คำพูด"))
    voice_channel = bot.get_channel(channel_id)
    print(text+" <------")
    global gTTS
    speech = gTTS (text = text,lang="th" , slow = True)
    speech.save("audio.mp3")
    vc = await voice_channel.connect()
    vc.play(discord.FFmpegPCMAudio("audio.mp3"), after=lambda e: print("เสร็จละ"))
    counter = 0
    cwd = os.getcwd()
    duration = audio_len(cwd + "/audio.mp3") # In seconds
    while not counter >= duration:
        time.sleep(2)
        counter += 1


@bot.command() #สแปมเข้าออกช่อง
async def spam(ctx,count):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    count = int(count)
    for i in range(count):
        if voice_client == None:

            await channel.connect()
            time.sleep(0.5)
            await ctx.voice_client.disconnect()
            time.sleep(0.8)




@bot.command() #เปิดเพลง
async def เล่น(ctx,url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)
    if voice_client == None:
        await ctx.channel.send("เข้ามาละ")
        await channel.connect()
        voice_client = get(bot.voice_clients, guild = ctx.guild)
    YDL_OPTIONS = {'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'logtostderr': False,
        'quiet': True,
        'no_warnings': True,
        'default_search': 'auto',
        'source_address': '0.0.0.0'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    
    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']

        source = await discord.FFmpegOpusAudio.from_probe(URL, **FFMPEG_OPTIONS)
        voice_client.play(source)
        
        voice_client.is_playing()
        
    else:
        await ctx.channel.send("เพลงกำลังเล่นอยู่")
        return
      
      
      
      
      
      
      
      
@bot.command() #ควบคุมการเข้าออกของบอท
async def เข้า(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@bot.command()
async def ออก(context):
    await context.voice_client.disconnect()
@bot.command(pass_context = True)
async def ปิดระบบ(ctx):

    if ctx.message.author.id == ไอดีที่ได้รับการอนุญาติ:
        await ctx.send("กำลังปิดระบบ")
        await ctx.bot.logout()
    else:
        await ctx.send("คุณไม่สามารถใช้คำสั่งนี้ได้")
        
        
        
#ลิขสิทธิ์ source code โดย fifaak     
bot.run(token)
