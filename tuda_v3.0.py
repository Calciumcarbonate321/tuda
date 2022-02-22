from http.client import HTTPSConnection
from sys import stderr
from json import dumps,loads
from datetime import datetime
import time
import re
import random
import threading

from selenium.webdriver.common import by
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from config import *

commands=["pls scratch "]
items=[]

def cooldown():
    cd=int(input("Enter cooldown between commands(in seconds): "))
    return cd

file = open("config.txt")
text = file.read().splitlines()

if len(text) != 4 or input("Configure bot? (y/n)") == "y":
    if len(text) != 4:
        print("An error was found inside the info file, reconfiguring is required.")
    file.close()
    with open("config.txt", "w") as file:
        text = []
        text.append(input("User agent: "))
        text.append(input("Discord token: "))
        text.append(input("Discord channel URL: "))
        text.append(input("Discord channel ID: "))

        for parameter in text:
            file.write(parameter + "\n")

header_data = {
    "content-type": "application/json",
    "user-agent": text[0],
    "authorization": text[1],
    "host": "discordapp.com",
    "referrer": text[2]
}
print(header_data)

print("Messages will be sent to " + header_data["referrer"] + ".")

def connect():
    return HTTPSConnection("discordapp.com", 443)

em=em
pw=pw


while True:
    try:
        cd=cooldown()
    except:
        print("The cooldown should be an integer.")  
        continue
    break

numberOfTimes=int(input("Enter number of times: "))
channel_name=channel   
channel_id=channelid

options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options, executable_path=r'chromedriver.exe')
driver.get("https://www.discord.com/app")
time.sleep(2)

email = driver.find_element_by_name('email')
email.send_keys(em)
password=driver.find_element_by_name('password')
password.send_keys(pw)
password.send_keys(Keys.RETURN)

time.sleep(10)

a=driver.find_element_by_class_name('searchBarComponent-32dTOx')
a.click()
time.sleep(1)
b=driver.find_element_by_class_name('input-2VB9rf')
b.send_keys(channel_name)
b.send_keys(Keys.RETURN)

text_element =driver.find_element(By.XPATH,'//*[@id="app-mount"]').find_element(By.XPATH , './/div[@class="app-1q1i1E"]').find_element(By.XPATH,'.//div[@class="app-2rEoOp"]').find_element(By.XPATH,'.//div[@class="layers-3iHuyZ layers-3q14ss"]').find_element(By.XPATH,'.//div[@class="layer-3QrUeG baseLayer-35bLyl"]').find_element(By.XPATH,'.//div[@class="container-2lgZY8"]').find_element(By.XPATH , './/div[@class="base-3dtUhz"]').find_element(By.XPATH , './/div[@class="content-98HsJk"]').find_element(By.XPATH , './/div[@class="chat-3bRxxu"]').find_element(By.XPATH , './/div[@class="content-yTz4x3"]').find_element(By.XPATH , './/main[@class="chatContent-a9vAAp"]').find_element(By.XPATH , './/form[@class="form-2fGMdU"]').find_element(By.XPATH , './/div[1]').find_element(By.XPATH , './/div[1]').find_element(By.XPATH , './/div[@class="channelTextArea-rNsIhG channelTextArea-2VhZ6z"]').find_element(By.XPATH , './/div[@class="scrollableContainer-2NUZem webkit-HjD9Er"]').find_element(By.XPATH , './/div[@class="inner-MADQqc sansAttachButton-td2irx"]').find_element(By.XPATH , './/div[@class="textArea-12jD-V textAreaSlate-1ZzRVj slateContainer-3Qkn2x"]').find_element(By.XPATH , './/div[@class="markup-2BOw-j slateTextArea-1Mkdgw fontSize16Padding-3Wk7zP"]')




def get_msg_id(conn, channel_id):
    try:
        channel = conn.request("GET", f"/api/v6/channels/{channel_id}/messages", headers=header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            a=loads(resp.read())
            return a[0]["id"]

        else:
            stderr.write(f"While checking message, received HTTP {resp.status}: {resp.reason}\n")
    except Exception as e:
        print(e)

def get_button_list(msgid):
    while True:
        b=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(1) .component-1IAYeC:nth-child(1)"
        try:
            driver.find_element(By.CSS_SELECTOR,b)
        except:
            msgid=get_msg_id(connect(),channel_id)
        else:
            break
    b1=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(1) .component-1IAYeC:nth-child(1)"
    b2=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(1) .component-1IAYeC:nth-child(2)"
    b3=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(1) .component-1IAYeC:nth-child(3)"
    b4=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(2) .component-1IAYeC:nth-child(1)"
    b5=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(2) .component-1IAYeC:nth-child(2)"
    b6=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(2) .component-1IAYeC:nth-child(3)"
    b7=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(3) .component-1IAYeC:nth-child(1)"
    b8=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(3) .component-1IAYeC:nth-child(2)"
    b9=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(3) .component-1IAYeC:nth-child(3)"
    b10=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(4) .component-1IAYeC:nth-child(1)"
    b11=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(4) .component-1IAYeC:nth-child(2)"
    b12=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(4) .component-1IAYeC:nth-child(3)"
    b13=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(5) .component-1IAYeC:nth-child(1)"
    b14=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(5) .component-1IAYeC:nth-child(2)"
    b15=f"#message-accessories-{msgid} .container-2xsjOj:nth-child(5) .component-1IAYeC:nth-child(3)"
    blistcss=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15]
    choosen_buttons=random.sample(blistcss,3)
    print(choosen_buttons)
    buttons=[]
    for i in choosen_buttons:
        buttons.append(driver.find_element(By.CSS_SELECTOR,i))
    return buttons

class daily:
    def __init__(self) -> None:
        self.isdaily=False

dailyclass=daily()

def wait_for_daily_to_get_over():
    time.sleep(600)
    dailyclass.isdaily=False

def send_messages():
    for _ in range(numberOfTimes):
        if not dailyclass.isdaily:
            text_element.send_keys("pls use daily")
            text_element.send_keys(Keys.ENTER)
            time.sleep(4)
            dailyclass.isdaily=True
            dailythread=threading.Thread(target=wait_for_daily_to_get_over)
            dailythread.start()

        for j in commands:
            bamount=str(random.randint(1000,10000))
            j=j+bamount
            text_element.send_keys(j)    
            time.sleep(1)        
            text_element.send_keys(Keys.ENTER)
            text_element.send_keys(Keys.ENTER)
            time.sleep(2)
            a=get_msg_id(connect(),channel_id)
            bt=get_button_list(a)
            for i in bt:
                print("clicked")
                time.sleep(1)
                i.click()
                i.click()
                time.sleep(0.5)
        time.sleep(1.5)
        if a:=random.randint(0,1):
            text_element.send_keys("pls bal")
            text_element.send_keys(Keys.ENTER)
        time.sleep(1)
        print(f"Ran {_+1} times")    
        time.sleep(cd+1)
send_messages()
