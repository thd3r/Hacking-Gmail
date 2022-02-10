#!/usr/bin/env python3
import sys

try:
    from telebot import types
    import telebot
    from colorama import Fore
    from bot.API import API_KEY
except ImportError:
    print(Fore.RED + "Please install library \n command > python3 -m pip install -r requirments.txt" + Fore.WHITE)

bot = telebot.TeleBot(API_KEY, parse_mode=None)

try:
    @bot.message_handler(commands=['start'])
    def send_start_message(msg):
        bot.reply_to(msg, "Hacking-Gmail tool is for Eductaional purpose only. Use /help for more info")
        global user_id
        user_id = msg.chat.id

    @bot.message_handler(commands=['GetCode'])
    def send_code_message(msg):
        bot.reply_to(msg, "The password is: 999666")
        global user_id
        user_id = msg.chat.id

    @bot.message_handler(commands=['exit'])
    def send_code_message(msg):
        bot.reply_to(msg, "Good bye!")
        bot.stop_polling()
        global user_id
        user_id = msg.chat.id

    @bot.message_handler(commands=['help'])
    def send_help_message(msg):
        bot.reply_to(msg, "Use /menu for menu window. Use /GetCode to get password. Use /exit to exit the bot program")
        global user_id
        user_id = msg.chat.id

    @bot.message_handler(commands=['menu'])
    def show_menu_page(msg):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn1 = types.KeyboardButton("/start")
        btn2 = types.KeyboardButton("/GetCode")
        btn3 = types.KeyboardButton("/help")
        btn4 = types.KeyboardButton("/exit")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(chat_id=msg.chat.id, text="Choose from menu", reply_markup=markup)

    print("Bot starting...")
    bot.polling()

except KeyboardInterrupt:
    print("")
    sys.exit()



