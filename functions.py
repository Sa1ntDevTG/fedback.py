# Слито в https://t.me/HACKER_PHONE_VIP

import sqlite3
from config import admin

# Слито в https://t.me/HACKER_PHONE_VIP

connection = sqlite3.connect('data.db')
q = connection.cursor()

# Слито в https://t.me/HACKER_PHONE_VIP

def join(chat_id):
    q.execute(f"SELECT * FROM users WHERE user_id = {chat_id}")
    result = q.fetchall()
    if len(result) == 0:
        sql = 'INSERT INTO users (user_id, block) VALUES ({}, 0)'.format(chat_id)
        q.execute(sql)
        connection.commit()

# Слито в https://t.me/HACKER_PHONE_VIP

async def antiflood(*args, **kwargs):
    m = args[0]
    if m.chat.id == admin:
    	pass
    else:
    	await m.answer("*🚫Сработал антифлуд!*🚫\n\nПрекрати флудить и жди 3 секунды!", parse_mode= 'Markdown')

# Слито в https://t.me/HACKER_PHONE_VIP