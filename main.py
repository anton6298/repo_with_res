import telebot, os
import pyttsx3
from telebot import types
bot = telebot.TeleBot('5019523292:AAG_gNqgrXtiLF-4r2dfKV06kBLSJ8lzryU')
eng = pyttsx3.init()

button_start = types.KeyboardButton('/help')

start_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_kb.add(button_start)

button_say = types.KeyboardButton('Скажи')
button_help = types.KeyboardButton('/help')

help_kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_kb.add(button_say)
help_kb.add(button_help)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет! Напиши /help чтобы посмотреть список команд!", reply_markup=start_kb)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет! Список команд: \n\n •Скажи \n\n •/help", reply_markup=help_kb) 
    elif message.text.lower() == "скажи":
        bot.send_message(message.from_user.id, "Введи фразу, которую нужно озвучить!")
        bot.register_next_step_handler(message, speech)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю! Напиши /help чтобы посмотреть список команд!", reply_markup=start_kb)

def speech(message):
    eng.save_to_file(message.text, "C:/Users/Наталья/Documents/python/bot/send.mp3")
    eng.runAndWait()
    try:
        f=open("C:/Users/Наталья/Documents/python/bot/send.mp3", "rb")
        #bot.send_audio(message.from_user.id, f, reply_markup=help_kb, title="Сделано с помощью @TTS_botbot")
        bot.send_voice(message.from_user.id, f, reply_markup=help_kb, caption="Создано с помощью @TTS_botbot")
        f.close()
        os.remove("C:/Users/Наталья/Documents/python/bot/send.mp3")
    except:
        bot.send_message(message.from_user.id, "Ошибка! Попробуйте снова!")

bot.polling(none_stop=True, interval=0)