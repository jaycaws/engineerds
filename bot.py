import discord
import 

class MyClient(discord.Client):
    def __init__(self):
        self.activeChannels = [
            {
                id:"engineerds",
                player:"*",
                state:None
            }
        ]
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print(message.channel.id)
        for channel in self.activeChannels:
            if message.channel.id == channel.id:
                if channel.state == None:
                    self.process_command(message)
                else:
                    self.startNims(message)

    

    async def process_command(message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def startNims(message):
        print('We starting nims bitches')

client = MyClient()
client.run('')
