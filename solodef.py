import telebot
import json

def get_cfg():
    with open('bot.cfg', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config



