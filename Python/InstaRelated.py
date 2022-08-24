from datetime import datetime
from itertools import dropwhile, takewhile

import instaloader

L = instaloader.Instaloader()

posts = instaloader.Profile.from_username(L.context, "soroushm.babaei").get_posts()

SINCE = datetime(2020, 7, 7)
UNTIL = datetime(2021, 7, 8)

for post in takewhile(lambda p: p.date > UNTIL, dropwhile(lambda p: p.date > SINCE, posts)):
    print(post.date)
    L.download_post(post, "soroushm.babaei")