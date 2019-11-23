import discord

class MyClient(discord.Client):
    def __init__(self):
        super().__init__();
        self.activeChannels = [
            {
                "id":630802065148608512,
                "player":"*",
                "state":None
            }
        ]
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        for channel in self.activeChannels:
            if message.channel.id == channel["id"]:
                if channel["state"] == None:
                    await self.process_command(message)
                else:
                    await self.nims(channel)
            else:
                print("Cancelled")


    

    async def process_command(self,message):
        if message.content.split()[0] == "nims":
            #Create NIMS Instance
            #channel = self.create('cool-channel');
            channel = "that one bitch";

            self.activeChannels.push({
                "id":channel.id,
                "player":message.author.name,
                "state":Nims()
            })
    async def nims(self,channel):
        print('We starting nims bitches')

client = MyClient()
client.run('NjQ3NTkyMjI5LTw1KexhUnhjrtww2n2E')
