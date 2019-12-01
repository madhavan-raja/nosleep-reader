import praw
import json
import random
import markdown2

creds = json.load(open("credentials.json"))

LIMIT = 100


def get_content():
    reddit = praw.Reddit(client_id=creds['client_id'], client_secret=creds['client_secret'], username=creds['username'], password=creds['password'], user_agent=creds['user_agent'])
    sub = reddit.subreddit('nosleep')
    sub_hot = sub.hot(limit=LIMIT)

    random_post = random.choice(list(sub_hot))

    body = markdown2.markdown(random_post.selftext)

    return random_post.author.name, random_post.title, random_post.url, random_post.upvote_ratio * 100, body

get_content()