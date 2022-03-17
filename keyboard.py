# Слито в https://t.me/HACKER_PHONE_VIP

from aiogram import types

# Слито в https://t.me/HACKER_PHONE_VIP

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.add(
    types.KeyboardButton('💈Админка💈')
)

# Слито в https://t.me/HACKER_PHONE_VIP

adm = types.ReplyKeyboardMarkup(resize_keyboard=True)
adm.add(
    types.KeyboardButton('👿 ЧС'),
    types.KeyboardButton('✅ Добавить в ЧС'),
    types.KeyboardButton('❎ Убрать из ЧС')
)
adm.add(types.KeyboardButton('💬 Рассылка'))
adm.add('↩️ Назад')

# Слито в https://t.me/HACKER_PHONE_VIP

back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back.add(
    types.KeyboardButton('↩️ Отмена')
)

# Слито в https://t.me/HACKER_PHONE_VIP

def fun(user_id):
    quest = types.InlineKeyboardMarkup(row_width=3)
    quest.add(
        types.InlineKeyboardButton(text='💬 Ответить', callback_data=f'{user_id}-ans'),
        types.InlineKeyboardButton(text='❎ Удалить', callback_data='ignor')
    )
    return quest

# Слито в https://t.me/HACKER_PHONE_VIP