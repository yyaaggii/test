import discord
import time
import random   
from bot_mantik import gen_pass
from bot_mantik import emoji_olusturucu

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

money = 0
moneyadd = 0
aura = 0

@client.event
async def on_ready():#bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):#Sunucudaki herhangi bir kanalda bir mesaj gönderildiğinde tetiklenir.
    global money, moneyadd, aura
    if message.author == client.user:
        return
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('emoji'):
        await message.channel.send(emoji_olusturucu())
    elif message.content.startswith("dünyayı koruyalım"):
        await message.channel.send("yere çöp atmayalım ve dünyamızı koruyalım!")
    elif message.content.startswith("cevreyi koruyalım"):
        await message.channel.send("ormanlara cam vb. çöpler atmayalım!")
    elif message.content.startswith("canlılar koruyalım"):
        await message.channel.send("hayvan bitki ve insanların yaşam kaynağı doğayı yok etmeyelim")
    elif message.content.startswith("nasılsın"):
        await message.channel.send("İyiyim sen nasılsın?")
    elif message.content.startswith("nerelisin?"):
        await message.channel.send("Ben bir bot olduğum için doğduğum yer yok. Ama sahibim türktür.")
    elif message.content.startswith("hikaye?"):
        await message.channel.send("https://popartistic.com/kisa-hikaye-ornekleri/ buradan efsane hikayeler bulabilirsin :D benim favorim /kum saati/ ;)")
    elif message.content.startswith("lets go gambling"):
        x = random.randint(1,2)
        if x == 1:
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("(+10000 money)aw dang i...")
            time.sleep(1.2)
            await message.channel.send("Wait ı won. I actually WON!")
            money = money + 10000
        elif x == 2:
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("aw dang it")
            await message.channel.send("OK IM DONE")
    elif message.content.startswith('yazı'):
        x = random.randint(1, 2)
        if x == 1:
            await message.channel.send("Doğru bildin")
        else:
            await message.channel.send("Yanlış bildin :(")
    elif message.content.startswith('tura'):
        x = random.randint(1, 2)
        if x == 2:
            await message.channel.send("Doğru bildin")
        else:
            await message.channel.send("Yanlış bildin :(")
    elif message.content.startswith('roll'):
        moneyadd = random.randint(100, 500)
        money = money+moneyadd
        await message.channel.send("u got some money")
    elif message.content.startswith("money"):
        await message.channel.send(money)
    elif message.content.startswith("buy aura"):
        if money > 500:
            await message.channel.send("wow u got good aura (+1000 aura)")
            aura = aura+1000
            money = money-500
        else:
            await message.channel.send("wow u lose good aura poor (-500 aura)")
            await message.channel.send("NOT ENOUGHT MONEY (NEED 500)")
            aura = aura-500
    elif message.content.startswith("aura"):
        await message.channel.send(aura)
    elif message.content.startswith('sifre'):
        await message.channel.send(gen_pass(5))
    else:
        await message.channel.send(message.content)
    
client.run("token")
