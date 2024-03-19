from telebot.types import Message

from loder import bot
from keyboart import start_btn

@bot.message_handler(commands=['start'])
def reaction_start(message:Message):
    ch_id = message.chat.id
    bot.send_message(ch_id, f'Asalomu alekom 😁 {message.from_user.full_name} iloji boricha yordam beraman',reply_markup=start_btn())
