import sys
import time
import random
import datetime
import telepot

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    
    print('Got command: %s' % command)
    
    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/logo':
        bot.sendPhoto (chat_id, photo = "https://1000logos.net/wp-content/uploads/2020/08/Telegram-Logo.png")
        
bot = telepot.Bot('Use this token to access the HTTP API:')
bot.message_loop(handle)
print('I am listening...')

while 1:
    time.sleep(10)
    

