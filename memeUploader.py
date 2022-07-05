import praw
import random
from random import randint
import requests
import shutil




reddit = praw.Reddit(client_id = "XXXXXXXXXXXXXXXXXXX",
                      client_secret= "XXXXXXXXXXXXXXXXXXXXXXX",
                      username="DaT1dUdE05",
                      password= "XXXXXXXXXXXXXXXXXX",
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


