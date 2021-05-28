import discord
from discord.ext import commands
from language import *

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        
        if not message.content.startswith("Message"):
            '''
            n_o_errors = numberOfErrors(str(message.content))
            ret_message = ('There are', n_o_errors, 'grammatical or spelling errors in your message')
            print(ret_message)
            if n_o_errors != 0:
                await message.reply(ret_message)
            '''
            return_message = str(checkText(str(message.content)))

            return_message_lines = return_message.splitlines()

            to_send = (', '.join(to_send[1:3]))

            print(to_send)
            await message.reply(to_send)

        if message.content.startswith('\u203Dreset'):
            if str(message.author) == "Micah#2740":
                add_to = open("/home/pi/Desktop/DiscordBot/count.txt", "w")
                add_to.write("0")
                add_to.close()
                await message.reply("And from the sky, the number hath been stricken back to 0")
            else:
                await message.reply("I'm afraid I can't do that, Dave")

        elif message.content.startswith("\u203Dreplier"):
            reply = input("reply: ")
            await message.reply(reply)
            
        elif message.content.startswith('\u203Doff'):
            await message.reply("Wrong")

        elif message.content.startswith('\u203D'):
            count = open("/home/pi/Desktop/DiscordBot/count.txt", "r")
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

            add_to = open("/home/pi/Desktop/DiscordBot/count.txt", "w")
            add_to.write(str(current_count))

            await message.reply("The total dislike of the new Discord is {}".format(current_count), mention_author=True)
            print(message.content)

        elif message.content.startswith('hack the mainframe'):
            if str(message.author) == "Micah#2740":
                await message.reply("Access granted, hacking now")
            else:
                await message.reply("You are not worthy")



client = MyClient()

keyfile = open("/home/pi/Desktop/DiscordBot/key.txt", "r")

logon_key = str(keyfile.read())

client.run(logon_key)
