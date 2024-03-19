from telebot.types import Message, ReplyKeyboardRemove
from loder import bot
from keyboart import *
import wikipedia


@bot.message_handler(func=lambda message: message.text == 'Bot haqida🤖')
def rteaction_start_btn(message: Message):
    ch_id = message.chat.id
    bot.send_message(ch_id, 'Bu bot sizga malumot olishda yordam beradi 👍 yordamimiz tekgan bolsa hursandmiz🙂 ')

@bot.message_handler(func=lambda message: message.text =="Muammolar bor🔧")
def reaction_muamo(message: Message):
    ch_id = message.chat.id
    bot.send_message(ch_id, "Muammolar bor bolsa🤝 @wttv_bot_admin ga murojat qiling👌")




@bot.message_handler(func=lambda message:message.text=='Malumot uchun🧐')
def reaction_wikipedia_malumot(message: Message):
    chat_id = message.chat.id
    svg = bot.send_message(chat_id, f"Qanday malumot kerak {message.from_user.full_name} ")
    bot.register_next_step_handler(svg, wikipedia_ku)


wikipedia.set_lang('uz')
wikipedia.set_lang('ru')
wikipedia.set_lang('eng')
def wikipedia_ku(message: Message):
    final = message.text
    try:
        mess = wikipedia.summary(final)
        chat_id = message.chat.id

        bot.send_message(chat_id, '⏳', reply_markup=ReplyKeyboardRemove())
        bot.delete_message(chat_id, message.id + 1)
        bot.send_message(chat_id, mess ,reply_markup=main_menyu())
    except:
            bot.send_message(message.chat.id, f"Afsuski bunday narsa topolmadim🥲 {message.from_user.full_name}" )





