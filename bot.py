import os
from mongoengine import connect
from models import Animation
import random
import wxpy

connect('db', host=os.getenv("MONGO_URI", "mongodb://localhost/db"))

def get_character():
    count = Animation.objects.count()
    rd =random.randint(0, count)
    animation = Animation.objects[rd:rd+1][0]
    return animation.movie_name, random.choice(animation.characters)

bot = wxpy.Bot(console_qr=True)

group = bot.groups()

@bot.register(chats=bot.groups()+bot.friends())
def reply_random_character(msg):
    if msg.type == wxpy.TEXT and "/random" in msg.text:
        movie_name, character = get_character()
        return "{} -- {}".format(character, movie_name)

bot.join()