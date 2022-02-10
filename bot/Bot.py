#!/usr/bin/rnv python3

i=ImportError
V=print
X=KeyboardInterrupt
import sys
W=sys.exit
try:
 import telebot
 from colorama import Fore
except i:
 V(Fore.RED+"Please install library \n command > python3 -m pip install -r requirments.txt"+Fore.WHITE)
 W()
y='5288572885:AAHULSvKBVo1zKx4TlW5-ifjfHZkLnyuWlc'
U=telebot.TeleBot(y)
try:
 @U.message_handler(commands=['start'])
 def J(message):
  U.reply_to(message,"Hi there!")
 @U.message_handler(commands=['help'])
 def J(message):
  U.reply_to(message,"""
Use /GetCode to get password
Use /exit to exit the bot program
"""  )
 @U.message_handler(commands=['GetCode'])
 def J(message):
  U.reply_to(message,"The password is: 999666")
 @U.message_handler(commands=['exit'])
 def J(message):
  U.reply_to(message,"Good Bye!")
  U.stop_polling()
 V("Bot Starting...")
 U.polling()
except X:
 V("")
 W()

