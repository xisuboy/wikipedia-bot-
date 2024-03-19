from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton

def start_btn():
    markub = ReplyKeyboardMarkup(resize_keyboard=True)
    markub.add(
        KeyboardButton('Bot haqida🤖'),
        KeyboardButton('Muammolar bor🔧'),
        KeyboardButton('Malumot uchun🧐')
    )
    return markub

def main_menyu():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        KeyboardButton('Bot haqida🤖'),
        KeyboardButton('Muammolar bor🔧'),
        KeyboardButton('Malumot uchun🧐')
    )
    return markup
