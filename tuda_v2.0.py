from http.client import HTTPSConnection
from sys import stderr
from json import dumps,loads
from datetime import datetime
from random import random
import time
import re
import random

file = open("config.txt")
text = file.read().splitlines()

if len(text) != 4 or input("Configure bot? (y/n)") == "y":
    if len(text) != 4:
        print("An error was found inside the info file, reconfiguring is required.")
    file.close()
    file = open("config.txt", "w")
    text = []
    text.append(input("User agent: "))
    text.append(input("Discord token: "))
    text.append(input("Discord channel URL: "))
    text.append(input("Discord channel ID: "))

    for parameter in text:
        file.write(parameter + "\n")

    file.close()

header_data = {
    "content-type": "application/json",
    "user-agent": text[0],
    "authorization": text[1],
    "host": "discordapp.com",
    "referrer": text[2]
}

print("Messages will be sent to " + header_data["referrer"] + ".")

def connect():
    return HTTPSConnection("discordapp.com", 443)

def send_message(conn, channel_id, message):
    message_data = {
        "content": message,
        "tts": False
    }

    try:
        conn.request("POST", f"/api/v6/channels/{channel_id}/messages", dumps(message_data), header_data)
        resp = conn.getresponse()
        if 199 < resp.status < 300:
            pass
        else:
            stderr.write(f"While sending message, received HTTP {resp.status}: {resp.reason}\n")
            pass
    except:
        stderr.write("Failed to send_message\n")

def get_embed(conn, channel_id):

    channel = conn.request("GET", f"/api/v6/channels/{channel_id}/messages", headers=header_data)
    resp = conn.getresponse()

    if 199 < resp.status < 300:
        try:
            a=loads(resp.read())
            print(a)
            print(type(a))
            print(a[0]["id"])
        except Exception as e:
            print(e)
        
        resp_string = str(resp.read(600))

        return resp_string

    else:
        stderr.write(f"While checking message, received HTTP {resp.status}: {resp.reason}\n")
        pass

def copy_text():
    choice=[]
    try:
        response = get_embed(connect(), text[3])
        print(response)
        response = response.replace("\\ufeff", "")
        response = response.replace("\\", "")
        e=str(response)
        list=[e.start() for e in re.finditer("`", e)]
        for i in list:
            index=list.index(i)
            if index%2==0:
                secind=index+1
                sece=list[secind]
                choice.append(e[i+1:sece])
        print(choice)
        my_choice=random.randint(0,len(choice)-1)
        my_choice=choice[my_choice]
        if 'mels room' in choice:
            my_choice='mels room'
        elif 'area51' in choice:
            my_choice='area51'
        elif 'fridge' in choice:
            my_choice='fridge'
            
        send_message(connect(), text[3], my_choice)
        print("Activated text copy " + (datetime.now()).strftime("%H:%M:%S"))
    except:
        pass

def cycle(period, command_list):
    for command in command_list:
        send_message(connect(), text[3], command)
        time.sleep(1)
        copy_text()
        time.sleep(period)

def main():
    command_list = []
    while True:
        command = input("Add a command to the cycle (type START to stop adding commands and begin using the bot): ")
        if command == "START":
            break
        command_list.append(command)


    period = int(input("Seconds between each command: "))
    print("Grinding the bot... " + (datetime.now()).strftime("%H:%M:%S"))
    while True:
        cycle(period, command_list)
        time.sleep(45)

main()




