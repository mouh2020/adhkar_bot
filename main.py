from telebot import TeleBot
from config import *
import random,requests,time

bot = TeleBot(token=bot_token)

def get_random_dhikr() : 
    return requests.get("https://ayah.nawafdev.com/api/dekr?types=random&ignore_errors=true").json()["content"]

while True : 
    try : 
        time_to_wait = random.randint(time_from,time_to)*60
        for channel in channels : 
            dhikr = get_random_dhikr()
            print(dhikr)
            bot.send_message(chat_id=channel,
                             text=dhikr)
            time.sleep(1)
        time.sleep(time_to_wait)
    except :
        time.sleep(time_to_wait)
        pass