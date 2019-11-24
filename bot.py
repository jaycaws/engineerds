import discord
import nims

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
                    #verify user id
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

            return nims.step();
            
    async def nims(self,channel):
        #retun channel.state.step(channel.messag);

client = MyClient()
client.run('NjQ3NTkyMjI5MTI4NjM0MzY5.Xdiaeg.bD4E30E9ZRRYp1H6C2oFqWzJjXc')
