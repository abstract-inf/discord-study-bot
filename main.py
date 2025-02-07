'''
This file is the main file for the bot. It contains the main logic for the bot to function.
The bot is able to respond to messages; by calling the find_response function from messages_handler.py
The bot can log when a user starts and stops studying, and send gifs based on the time a user spent studying.

The bot is able to respond to messages 
The find_response function which is called from the messages_handler.py takes a message as input and returns a response based on the message.

In the on_message function, the bot checks if the message is a command to start or stop studying.
Or if the message should be handled by the messages_handler.py file.
'''

import discord
import os
import random
from dotenv import load_dotenv
import datetime
import asyncio
import messages_handler
import pandas as pd

# Create a DataFrame to store logs
studyLogsDF = pd.DataFrame(columns=['Name', 'Start Time', 'End Time', 'Time Spent'])
# Create a DataFrame to store channel logs
channelLogsDF = pd.DataFrame(columns=['Channel','User', 'Time', 'isJoin'])  #isJoin is a boolean to indicate if the user joined or left the channel

# Use existing CSV logs file if it exists
if os.path.exists('study_logs.csv'):
    studyLogsDF = pd.read_csv('study_logs.csv')
    channelLogsDF = pd.read_csv('channel_logs.csv')
# Create a new CSV logs file if it doesn't exist
else:
    studyLogsDF.to_csv('study_logs.csv', index=False)
    channelLogsDF.to_csv('channel_logs.csv', index=False)

# Load environment variables
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

client = discord.Client(intents=intents)
is_studying = {}  # this dict has the name of the member as the key and a boolean indicating if they are studying as the value
study_start_times = {}  # this dict has the name of the member as the key and the time they started studying as the value
channel_logs_name = 'denshi-bot'

# Basic ANSI escape sequences for coloring the text in print statements
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"  # Purple color
CYAN = "\033[36m"  # Cyan color
WHITE = "\033[97m"  # White color
RESET = "\033[0m"  # Reset color

async def send_terminal_input():
    """Function to get input from the terminal and send it to Discord"""
    await client.wait_until_ready()  # Ensure bot is connected
    print(f"{GREEN}Bot is ready. Press 'Enter' to start sending terminal input.{RESET}")

    while True:
        # Wait for the user to press 'Enter' to start or re-enter terminal input mode
        await asyncio.to_thread(input, f"{YELLOW}Press 'Enter' to start or re-enter terminal input mode.{RESET}\n")

        print(f"{GREEN}Bot is now ready to receive terminal input.{RESET}")

        # Start the message input loop
        while True:
            user_input = await asyncio.to_thread(input, f"{YELLOW}Enter message to send: {RESET}")  # Run input() in a non-blocking way
            if user_input.strip():  # Check if the input is not empty
                target_channel = discord.utils.get(client.get_all_channels(), name="denshi-bot")

                if target_channel:
                    await target_channel.send(f"📢 **Console Message:** {user_input}")
                    print(f"{GREEN}✅ Sent to #{target_channel.name}:{RESET} {user_input}")
                else:
                    print(f"{RED}⚠️ Channel 'denshi-bot' not found.{RESET}")
            else:
                # If no input is provided, exit the input mode and return to waiting for 'Enter'
                print(f"{RED}⚠️ No input received, exiting input mode.{RESET}")
                break


@client.event
async def on_ready():
    print(f'{GREEN}Logged in as {client.user}{RESET}')
    asyncio.create_task(send_terminal_input())  # Start terminal input loop
    print('------')


# this function is called whenever a message is sent in the server
# this function is responsible for handling the message and responding to it
# this function also handles the case where a user wants to START or STOP studying
@client.event
async def on_message(message):
    global studyLogsDF
    # this is not to confuse the bot with its own messages
    if message.author == client.user:
        return

    # this is supposed to handle empty messages by ignoring them
    if message.content == '':  # ignore empty messages
        return
    
    # this is supposed to handle the case where the user wants to start studying
    if message.content.lower() in ['!study', '!start']:
        if message.author.name in is_studying and is_studying[message.author.name]:
            await message.channel.send(f"📚 <@{message.author.id}> is already studying.")
        else:
            is_studying[message.author.name] = True  # set the user as studying
            await message.channel.send(f"📚 <@{message.author.id}> has started studying.")
            print(f"{GREEN}{message.author.name} has started studying{RESET}")
            
            # log the time the user started studying
            study_start_times[message.author.name] = datetime.datetime.now()

            # create an embed to log the time the user started studying
            # this is simply a visual representation of the time the user started studying
            embed = discord.Embed(
                title=f"**{message.author.display_name} Started Studying**",
                color=discord.Color.blue()
            ).add_field(
                name='Time started Studying',
                value=f"**```{datetime.datetime.now().strftime('%I:%M:%S %p')}```**"
            )

            # send the embed to the channel
            await message.channel.send(embed=embed)
            print(f"{GREEN}Sent {YELLOW}studying start {GREEN}log for {PURPLE}{message.author.name} {RESET}[{datetime.datetime.now().strftime('%I:%M:%S %p')}]")


    # this is supposed to handle the case where the user wants to stop studying
    elif message.content.lower() in ['!stop', '!end']:
        # check if the user is studying
        # if they are studying, set them as not studying and log the time they stopped studying
        if message.author.name in is_studying and is_studying[message.author.name]:
            is_studying[message.author.name] = False
            await message.channel.send(f"🛑 <@{message.author.id}> has stopped studying.")
            print(f"{GREEN}{message.author.name} has stopped studying{RESET}")

            # log the time the user stopped studying
            start_time = study_start_times.pop(message.author.name)
            total_time = datetime.datetime.now() - start_time

            # format the time the user spent studying hours, minutes, and seconds
            hours, remainder = divmod(int(total_time.total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

            # log the time the user spent studying in CSV file
            # this is to keep track of the time the user spent studying
            studyLogsDF.loc[len(studyLogsDF)] = {'Name': message.author.name, 'Start Time': start_time, 'End Time': datetime.datetime.now(), 'Time Spent': total_time}
            studyLogsDF.to_csv('study_logs.csv', index=False)
            print(f"{GREEN}Logged studying time for {message.author.name}: {studyLogsDF.loc[len(studyLogsDF)-1]}{RESET}")


            # create an embed to log the time the user stopped studying
            # this is simply a visual representation of the time the user stopped studying
            embed = discord.Embed(
                title=f"**Total Time {message.author.display_name} Spent Studying**",
                color=discord.Color.blue()
            ).add_field(
                name='Time Spent Studying',
                value=f"**```{formatted_time}```**"
            ).set_image(url=get_appropriate_gif(hours, minutes))

            # send the embed to the channel
            await message.channel.send(embed=embed)
            print(f"{GREEN}Sent studying time log for {message.author.name}: {formatted_time}{RESET}")

        # if the user is not studying, send a message to the channel indicating that they are not studying
        else:
            await message.channel.send(f"🛑 <@{message.author.id}> is not studying.")
    
    else:
        msg = message.content.lower()
        print(f"[{message.channel}] {BLUE}Received message from {PURPLE}[{message.author}]:{RESET} {msg}")

        bot_response = messages_handler.find_response(msg)
        if bot_response:
            # check if the response is a file to respond appropriately
            try:
                if bot_response['file']:
                    await message.channel.send(file=discord.File(bot_response['file']))
            except:
                await message.channel.send(bot_response)
                print(f"{BLUE}Bot Response:{RESET} {bot_response}")
        

# this was supposed to handle the case where the user joins or leaves a voice channel
# now this function logs the time the user joins or leaves a voice channel
@client.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        # Avoid logging internal messages like "Voice state update"
        text_channel = discord.utils.get(member.guild.text_channels, name=channel_logs_name)

        # User joins a voice channel
        if before.channel is None and after.channel is not None:
            channelLogsDF.loc[len(channelLogsDF)] = {'Channel': after.channel.name, 'User': member.name, 'Time': datetime.datetime.now(), 'isJoin': True}
            channelLogsDF.to_csv('channel_logs.csv', index=False)
            # study_start_times[member.name] = datetime.datetime.now()
            # if text_channel:
                # embed = discord.Embed(
                #     title=f"**@{member.name} Started Studying**",
                #     color=discord.Color.blue()
                # ).add_field(
                #     name='Time started Studying',
                #     value=f"**```{datetime.datetime.now().strftime('%I:%M:%S %p')}```**"
                # )
                # await text_channel.send(embed=embed)
                # print(f"{GREEN}Sent {YELLOW}studying start {GREEN}log for {PURPLE}{member.name} {RESET}[{datetime.datetime.now().strftime('%I:%M:%S %p')}]")

        # User leaves a voice channel
        elif before.channel is not None and after.channel is None:
            # if member.name in study_start_times and text_channel:
            channelLogsDF.loc[len(channelLogsDF)] = {'Channel': before.channel.name, 'User': member.name, 'Time': datetime.datetime.now(), 'isJoin': False}
            channelLogsDF.to_csv('channel_logs.csv', index=False)
                # total_time = datetime.datetime.now() - study_start_times.pop(member.name)
                # hours, remainder = divmod(int(total_time.total_seconds()), 3600)
                # minutes, seconds = divmod(remainder, 60)
                # formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

                # embed = discord.Embed(
                #     title=f"**Total Time @{member.name} Spent Studying**",
                #     color=discord.Color.blue()
                # ).add_field(
                #     name='Time Spent Studying',
                #     value=f"**```{formatted_time}```**"
                # ).set_image(url=get_appropriate_gif(hours, minutes))
                # await text_channel.send(embed=embed)
                # print(f"{GREEN}Sent studying time log for {member.name}: {formatted_time}{RESET}")

def get_appropriate_gif(hours, minutes):
    # this dictionary contains the range of hours spent studying and the corresponding gif
    # the key is a tuple of the lower and upper bound of the range for hours spent studying and the value is the gif
    # (lower bound inclusive, upper bound exclusive): gif url
    gifs = {
        (0, 1): 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHo2eWZhdzgzdDFobHl1ejZyMDhwNXA5c2hiOXRqcXl3cjZ6ZjFmbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/W3Ch3vjHi5FGefDT0G/giphy.gif',
        (1, 2): 'https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExanhsZG8zN3E5NzIydDl1Y2M0ZDd6ZGd0dWZtbWJ3NGpvM2lncWFhbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/zHO316FmyqmZi/giphy.gif',
        (2, 5): 'https://media.discordapp.net/attachments/1252190332972437528/1273677577650704496/5_hours_spent.gif?ex=66bf7c2e&is=66be2aae&hm=39039aef968dd38fb7bb06320745f681ab6f45d246cd59bf45d41a9e2a910c7f&=&width=547&height=304',
        (5, 10): 'https://c.tenor.com/rOwSSoqgQ3QAAAAC/tenor.gif'
    }
    return next(gif for (lower, upper), gif in gifs.items() if lower <= hours < upper)


TOKEN = os.getenv('TOKEN')
client.run(TOKEN)
