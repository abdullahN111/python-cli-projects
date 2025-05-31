from instabot import Bot
from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

bot = Bot()


bot.login(username=username, password=password, is_threaded=True)
bot.follow("bettercallsubhan")