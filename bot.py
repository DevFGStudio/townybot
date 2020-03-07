import discord
import asyncio
import datetime
import os
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    game = discord.Game("환영하오 :D")
    await client.change_presence(status=discord.Status.online,activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("/예쁘지공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 예쁘지", icon_url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)


async def on_message(message):
    if message.content.startswith("/예쁘지처벌"):
        embed = discord.Embed(title=":warning: 제재 안내", color=0xFFFF24, description=" ")

        embed.set_field(name='닉네임:', vaule=''.join(message.content.split()[4:]))


        
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        channel = client.get_channel(int(message.content.split()[3]))

        
        embed.set_footer(text="담당 관리자 | 예쁘지", icon_url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)



    if message.content.startswith("/에이티오공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 에이티오", icon_url="https://cravatar.eu/head/A__TO/64.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)



    if message.content.startswith("/지엣지공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 지엣지", icon_url="https://cravatar.eu/head/Gold_Edge/64.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)



    if message.content.startswith("/쿵이공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 쿵이", icon_url="https://cravatar.eu/head/Jikung0925/64.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)




    if message.content.startswith("/밤공지"):
        embed = discord.Embed(title="안내사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="담당 관리자 | 밤", icon_url="https://cravatar.eu/head/BARMCO/64.png")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)



    if message.content.startswith("/관리자공지"):
        embed = discord.Embed(title="공지사항", color=0xFFFF24, description=" ".join(message.content.split()[2:]))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        channel = client.get_channel(int(message.content.split()[1]))
        embed.set_footer(text="타우니 관리자 일동", icon_url="https://cdn.discordapp.com/attachments/542651500116181002/685363931489107968/JPEG_20190911_170206.jpg")
        embed.timestamp = datetime.datetime.utcnow()

        await channel.send(embed=embed)
access_token = os.envirun["BOT_TOKEN"]
client.run(access_token) 
