import discord
from discord.ext import tasks
import asyncio
import random
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

commands=[
    "pls hunt",
    "pls fish",
    "pls beg",
    "pls dig",
    "pls slots {}".format(random.randint(1000,2000)),
    "pls se {}".format(random.randint(1000,50000)),
    "pls scratch 10k",
    "pls search",
    "pls crime"
]

class MyClient(discord.Client):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.toggle=False
        self.btcount=[]
        self.tudatoggle=False
        options = webdriver.ChromeOptions() 
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://discord.com/channels/820019529429811200/840848435435143188")
        time.sleep(2)
        email = self.driver.find_element(By.NAME,'email')
        email.send_keys(em)
        password=self.driver.find_element(By.NAME,'password')
        password.send_keys(pw)
        password.send_keys(Keys.RETURN)
        print("browser ready")

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.guild is None:
            return
        if message.author == self.user and message.guild.id == 820019529429811200:
            if message.content=="susybaka":
                if not self.toggle:
                    self.toggle=True
                    return await message.reply('Turned **on** the reactor boss☢')                            
                await message.reply('Turned **off** the reactor boss☢')
                self.toggle=False
            if message.content=="notsusbattlecountnotsus":
                try:
                    await message.reply("bt_link\n".join(self.btcount) or "None yet")
                except:
                    pass
                await message.channel.send(f"{len(self.btcount)} battles over")
            if message.content=="susautotypersus":
                if not self.tudatoggle:
                    self.tudatoggle=True
                    await message.reply("Started auto typer boss")
                    return autotyperloop.start()
                await message.reply("Stopped auto typer boss")
                autotyperloop.cancel()



    async def on_raw_reaction_add(self,payload):
        if payload.channel_id in [929418272342941696,868248817835847783]:
            if (
                payload.member.id == 693167035068317736
                and payload.emoji.id == 872886436012126279
            ):
                msg=await (self.get_channel(payload.channel_id)).fetch_message(payload.message_id)
                emb=msg.embeds[0]
                if 'Rumble Royale' in emb.title and len(msg.reactions) > 0:
                    emo=msg.reactions[0].emoji
                    await asyncio.sleep(random.randint(5,10))
                    await msg.add_reaction(emo)
                    self.btcount.append(msg.jump_url)

        elif payload.channel_id in [642045566230069249,693170559152029727,693170586934837310,903238915991945256] and self.toggle:
            if (
                payload.member.id == 693167035068317736
                and payload.emoji.id == 872886436012126279
            ):
                msg=await (self.get_channel(payload.channel_id)).fetch_message(payload.message_id)
                emb=msg.embeds[0]
                if 'Rumble Royale' in emb.title and len(msg.reactions) > 0:
                    emo=msg.reactions[0].emoji
                    await asyncio.sleep(90)
                    await msg.add_reaction(emo)
                    self.btcount.append(msg.jump_url)

client = MyClient(self_bot=True,status=discord.Status.dnd)

@tasks.loop(seconds=60)
async def autotyperloop():
    cc=client.get_channel(840848435435143188)
    for i in commands:
        if i.startswith('pls scratch'):
            await cc.send(i)
            msg=await client.wait_for('message',check=lambda m : m.channel.id==cc.id and m.author.id==270904126974590976)
            bt=await get_scratch_button_list(msg.id)
            blist=random.sample(bt,k=3)
            for i in blist:
                i.click()
                await asyncio.sleep(1)
            continue
        if i=="pls search":
            await cc.send(i)
            msg=await client.wait_for('message',check=lambda m : m.channel.id==cc.id and m.author.id==270904126974590976 and len(msg.embeds)>0)
            await asyncio.sleep(2)
            bt=await get_search_button_list(msg.id)
            bt[random.randint(0,2)].click()
            continue
        if i=="pls crime":
            await cc.send(i)
            msg=await client.wait_for('message',check=lambda m : m.channel.id==cc.id and m.author.id==270904126974590976 and len(msg.embeds)>0)
            await asyncio.sleep(2)
            bt=await get_search_button_list(msg.id)
            bt[random.randint(0,2)].click()
            continue
        await cc.send(i)
        await asyncio.sleep(random.randint(3,6))

async def get_scratch_button_list(msgid):

    base='//*[@id="message-accessories-{}"]/div[2]/div[{}]/div/button[{}]'
    l=[]
    for i in range(1,6):
        l.extend(base.format(msgid,i,j) for j in range(1,4))
    nl=[]
    for i in l:
        try:
            ee=client.driver.find_element(By.XPATH,i)
            nl.append(ee)
        except:
            pass
    return nl

async def get_search_button_list(msgid):
    base='//*[@id="message-accessories-{}"]/div/div/div/button[{}]'
    l = [base.format(msgid,i) for i in range(1,4)]
    nl=[]
    for i in l:
        try:
            ee=client.driver.find_element(By.XPATH,i)
            nl.append(ee)
        except:
            pass
    return nl

client.run(token)
