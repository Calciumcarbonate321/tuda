from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

items=[]
commands=[]

def cooldown():
    cd=int(input("Enter cooldown between commands(in seconds): "))
    return cd

em=input("Enter your discord email id: ")
pw=input("Enter your discord password: ")

istransfer=input("Type 'Y', if you are going to transfer inventory items,type C if you are going to use cheese: ")

if istransfer in ['Y','y']:
    alt=input("Enter the name of your alt account(if my alt account name was Darth-diabetes I would enter @Darth-diabetes): ")
    k=0
    while True:
        temp=input("Enter item name along with the number of items(amount,items): ")
        if temp in ['N','n','Exit']:
            break
        items.append(temp)
        temp=str()
elif istransfer in ['C','c']:
    commands='pls use cheese'
    y='y'
    numberOfTimes=int(input("How many cheese do you want to use: "))
else:
    while True:
        try:
            cd=cooldown()
        except:
            print("The cooldown should be an integer.")  
            continue
        break
    while True:
        c=input("What commands do you want to spam?(hit enter after one command),press n and then enter to proceed:  ")
        if c in ['n','N']:
            break
        commands.append(c)
    numberOfTimes=int(input("Enter number of times: "))
channel_name=input("Enter channel name (if my channel name was hello I would enter #hello): ")    


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

if istransfer in ['Y','y']:
    for i in items:
        text_element.send_keys("pls gift ",i," ",alt)
        text_element.send_keys(Keys.ENTER)
        text_element.send_keys(Keys.ENTER)
        time.sleep(21)
    print("Job done")
elif istransfer in ['C','c']:
    for i in range(numberOfTimes):
        text_element.send_keys('pls use cheese')  
        text_element.send_keys(Keys.ENTER)
        text_element.send_keys(Keys.ENTER)
        time.sleep(1)
        text_element.send_keys('y')
        text_element.send_keys(Keys.ENTER)
        text_element.send_keys(Keys.ENTER)
        time.sleep(6)
    print("Job done")        
else:
    for i in range(numberOfTimes):
        for j in commands:

            text_element.send_keys(j)    
            time.sleep(2)        
            text_element.send_keys(Keys.ENTER)
            text_element.send_keys(Keys.ENTER)
            time.sleep(1)
        time.sleep(cd+1)

print("Job is done my lord!")
driver.close()
