import praw
import random
from random import randint
import requests
import shutil
import os
import time




reddit = praw.Reddit(client_id = "",
                      client_secret= "",
                      username="DaT1dUdE05",
                      password= "",
                      user_agent="pythonmeme",
                      check_for_async=False
                    )



subreddit= reddit.subreddit("AskReddit")


all_subs= []



count = 1
for i in range(1):


    top = subreddit.hot(limit = 100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)


    res = requests.get(random_sub.url, stream = True)

    if res.status_code == 200:
         with open("C:\Stories\story"+str(count),'wb') as f:
            shutil.copyfileobj(res.raw, f)

    count+=1

    print(random_sub.url)
    print(random_sub.title)
    print("Done.")

url = random_sub.url
submission = reddit.submission(url = url)

comments = []

num = 5
submission.comments.replace_more(limit=None)
for top_level_comment in submission.comments:
    if num>0:
        print(top_level_comment.body)
        comments.append(top_level_comment.body)
        print()
    num-=1


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service



#Finding and taking screenshot of question   
path=Service("C:\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get(url)

driver.maximize_window()


import pyautogui

myscreen = pyautogui.screenshot(region=(1000,600,1200,350))

myscreen.save('C:\Stories\q.png')
print("image saved")

driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://translate.google.com/')

#Finding Text Area to Type in
#for i in comments:
driver.find_element(By.XPATH,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys(random_sub.title)
driver.find_element(By.XPATH,'//*[@id="i8"]/span[3]').click()
time.sleep(5)
#driver.find_element(By.XPATH,'//*[@id="ow87"]/div/span/button/div[3]').click()
#time.sleep(2)
    


from pywinauto.application import Application

app = Application(backend='uia').start('C:\Program Files\Audacity\Audacity.exe').connect(title = 'Audacity', timeout = 5)

#app.Audacity.print_control_identifiers()

rec = app.Audacity.child_window(title="Record", auto_id="11005", control_type="Button").wrapper_object()
rec.click()







