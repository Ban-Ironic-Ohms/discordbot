import discord
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('\u203Dreset'):
            if str(message.author) == "Micah#2740":
                add_to = open("C:/Users/Micah/Desktop/Personal/Python/count.txt", "w")
                add_to.write(0)
                add_to.close()

            await message.reply("I'm afraid I can't do that, Dave")

        elif message.content.startswith('\u203Doff'):
            await message.reply("Wrong")

        elif message.content.startswith('\u203D'):
            count = open("C:/Users/Micah/Desktop/Personal/Python/count.txt", "r")
            try:
                current_count = int(count.read())
            except ValueError:
                current_count = 0
            count.close()

            user_content = message.content[1:]

            try:
                user_content = int(user_content)
            except TypeError:
                return


            current_count += user_content

            add_to = open("C:/Users/Micah/Desktop/Personal/Python/count.txt", "w")
            add_to.write(str(current_count))

            await message.reply(f'The total dislike of the new Discord is {current_count}', mention_author=True)
            print(message.content)

client = MyClient()

keyfile = open("C:/Users/Micah/Desktop/Personal/Python/key.txt", "r")

logon_key = str(keyfile.read())

client.run(logon_key)