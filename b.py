
import telebot
import logging
import subprocess
from pymongo import MongoClient
from datetime import datetime, timedelta
import certifi
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

from keep_alive import keep_alive
keep_alive()

TOKEN = '7376682624:AAFuZXujuqAtJaMB8jdZRTCHif8RpwbcH3Y'
MONGO_URI = 'mongodb+srv://MasterBhaiyaa:MasterBhaiyaa@masterbhaiyaa.7bym6.mongodb.net/?retryWrites=true&w=majority&appName=MasterBhaiyaa'
CHANNEL_ID = -1002255025786
ADMIN_IDS = [1866816118]

client = MongoClient(MONGO_URI, tlsCAFile=certifi.where())
db = client['MasterBhaiyaa']
users_collection = db.users
bot = telebot.TeleBot(TOKEN)
blocked_ports = [8700, 20000, 443, 17500, 9031, 20002, 20001]
user_attack_details = {}
active_attacks = {}

