import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Bot fai iniciade :D')

    async def on_message(self, message):
        if message.content == 'ping':
            await message.channel.send(':ping_pong: pong')


client = MyClient()
client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
