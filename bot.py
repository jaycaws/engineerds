import discord
import nims
import datetime
import json

class MyClient(discord.Client):
    def __init__(self):
        super().__init__();
        self.activeChannels = [
            {
                "channel": None,
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
                    await self.process_command(channel,message)
                else:
                    if channel["player"] == message.author.id:
                        await self.nims(channel,message)
                    else:
                        pass                        

    

    async def process_command(self,channel,message):
        if message.content.split()[0] == "nims":
            guild = message.guild
            newChannel = await guild.create_text_channel('nims-' + message.author.name )
            
            self.activeChannels.append({
                "channel":newChannel,
                "id":newChannel.id,
                "player":message.author.id,
                "state":nims.Nims()
            })

            await newChannel.send(self.activeChannels[len(self.activeChannels)-1]["state"].step(None));


    async def nims(self,channel,message):
        await channel["channel"].send(channel["state"].step(message.content))
        if channel["state"] is None:
            await channel.send("Removing session in 5 seconds...")
            time.sleep(5)
            self.activeChannels.remove(channel)
            await channel["channel"].delete("We finished the game bitches")

with open('./keys.json', 'r') as myfile:
    data=myfile.read()

# parse file
keys = json.loads(data)

token = keys["token"]


client = MyClient()
client.run(token)
