import praw
import random
from random import randint
import requests
import shutil
import os




reddit = praw.Reddit(client_id = "*",
                      client_secret= "*",
                      username="DaT1dUdE05",
                      password= "*",
                      user_agent="pythonmeme",
                      check_for_async=False
                    )

all_subred = []

subreddit1 = reddit.subreddit("dankmemes")
subreddit2 = reddit.subreddit("meme")
subreddit3 = reddit.subreddit("memes")
subreddit4 = reddit.subreddit("HistoryMemes")
all_subred.append(subreddit1)
all_subred.append(subreddit2)
all_subred.append(subreddit3)
all_subred.append(subreddit4)

subreddit = random.choice(all_subred)

all_subs= []

file_path1 = r'C:\Memes\meme1.gif'
file_path2 = r'C:\Memes\meme1.jpg'
file_path3 = r'C:\Memes\meme2.gif'
file_path4 = r'C:\Memes\meme2.jpg'
file_path5 = r'C:\Memes\meme3.gif'
file_path6 = r'C:\Memes\meme3.jpg'
file_path7 = r'C:\Memes\meme4.gif'
file_path8 = r'C:\Memes\meme4.jpg'
file_path9 = r'C:\Memes\meme5.gif'
file_path10 = r'C:\Memes\meme5.jpg'
if os.path.exists(file_path1):
    os.remove(file_path1)
if os.path.exists(file_path2):
    os.remove(file_path2)
if os.path.exists(file_path3):
    os.remove(file_path3)
if os.path.exists(file_path4):
    os.remove(file_path4)
if os.path.exists(file_path5):
    os.remove(file_path5)
if os.path.exists(file_path6):
    os.remove(file_path6)
if os.path.exists(file_path7):
    os.remove(file_path7)
if os.path.exists(file_path8):
    os.remove(file_path8)
if os.path.exists(file_path9):
    os.remove(file_path9)
if os.path.exists(file_path10):
     os.remove(file_path10)

count = 1
for i in range(5):


    top = subreddit.hot(limit = 100)

    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    print(random_sub.url[-3:])

    res = requests.get(random_sub.url, stream = True)

    if res.status_code == 200:
        if random_sub.url[-3:] == "gif":
            with open("C:\Memes\meme"+str(count)+".gif",'wb') as f:
                shutil.copyfileobj(res.raw, f)
        elif (random_sub.url[-3:] == "jpg") or (random_sub.url[-3:] == "png"):
            with open("C:\Memes\meme"+str(count)+".jpg",'wb') as f:
                shutil.copyfileobj(res.raw, f)
        else:
            continue
    count+=1

    print(random_sub.url)
    print("Done.")


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service



    
path=Service("C:\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get('https://app.clipchamp.com/login')





