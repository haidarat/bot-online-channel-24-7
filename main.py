import os
import discord
from flask import Flask
from discord.ext import commands
from keep_alive import keep_alive


keep_alive()

intents = discord.Intents().all()
intents.members = True
intents.voice_states = True
intents.messages = True
intents.guilds = True
intents.reactions = True
intents.emojis = True
intents.presences = True

def create_bot():
    bot = commands.Bot(command_prefix='!', intents=intents)
    return bot

bot = create_bot()

@bot.event
async def on_ready():
    channel_id = int(os.environ.get('id'))
    await joinid(bot.get_channel(channel_id))

async def joinid(channel):
    """เรียกบอทเข้าห้องแบบกำหนด channel id"""
    if channel:
        if bot.voice_clients:
            await bot.voice_clients[0].move_to(channel)
        else:
            await channel.connect()
        print(f'เข้าห้อง {channel} เรียบร้อยแล้วค่ะ!')
    else:
        print('ไม่พบห้องที่ระบุ!')

@bot.command()
async def hello(ctx):
    await ctx.send('สวัสดีครับ!')

token = os.environ.get('token')
bot.run(token)
