import telebot
import random
from telebot import types

token = "664355609:AAGv5YabXVJJ8vy8dBapVxYlXHkLFQdCxts"


telebot.apihelper.proxy = {'https': 'socks5://tvorogme:TyhoRuiGhj1874@tvorog.me:6666'}

bot = telebot.TeleBot(token=token)

is_reg_open = dict.fromkeys(['chess', 'tennis'], 1) 
users_chess = {}
users_chess_next = {}
users_tennis = {}
users_tennis_next = {}

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, 'Это GoTo SportBot. Для участия в соревнованиях нажми /play')

@bot.message_handler(commands=['startChess'])
def startChess(message):
    global is_reg_open
    global users_chess
    is_reg_open['chess'] == 0
    random.shuffle(users_chess)
    if len(users_chess) == 0:
        return
    if len(users_chess) % 2 != 0:
        users_chess['fake'] = "fake"
    users_names = list(users_chess.values())
    users_ids = list(users_chess.keys())
    for i in range(0,len(users_chess)):
        text = "Вы играете с - " + str(users_names[i+1])
        bot.send_message(users_ids[i], text)
        text = "Вы играете с - " + str(users_names[i])
        bot.send_message(users_ids[i+1], text)
        
@bot.message_handler(commands=['startTennis'])
def startTennis(message):
    global is_reg_open
    global users_tennis
    is_reg_open['tennis'] == 0
    random.shuffle(users_tennis)
    if len(users_tennis) == 0:
        return
    if len(users_tennis) % 2 != 0:
        users_tennis['fake'] = "fake"
    users_names = list(users_tennis.values())
    users_ids = list(users_tennis.keys())
    for i in range(0,len(users_tennis)):
        text = "Вы играете с - " + str(users_names[i+1])
        bot.send_message(users_ids[i], text)
        text = "Вы играете с - " + str(users_names[i])
        bot.send_message(users_ids[i+1], text)
        
@bot.message_handler(commands=['chessOpen'])
def reg(message):
    global is_reg_open
    user = message.chat.id
    is_reg_open['chess'] = 1
    bot.send_message(user, 'Регистрация на шахматы открыта')

@bot.message_handler(commands=['tennisOpen'])
def reg(message):
    global is_reg_open
    user = message.chat.id
    is_reg_open['tennis'] = 1
    bot.send_message(user, 'Регистрация на теннис открыта')

@bot.message_handler(commands=['chessClose'])
def reg(message):
    global is_reg_open
    user = message.chat.id
    is_reg_open['chess'] = 0
    bot.send_message(user, 'Регистрация на шахматы закрыта')

@bot.message_handler(commands=['tennisClose'])
def reg(message):
    global is_reg_open
    user = message.chat.id
    is_reg_open['tennis'] = 0
    bot.send_message(user, 'Регистрация на теннис закрыта')
        
@bot.message_handler(commands=['play'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    user = message.chat.id
    button1 = types.InlineKeyboardButton(text='Шахматы', callback_data="button1")
    button2 = types.InlineKeyboardButton(text='Теннис', callback_data="button2")
    button3 = types.InlineKeyboardButton(text='Не участвовать', callback_data="button3")
    keyboard.add(button1)
    keyboard.add(button2)
    keyboard.add(button3)
    bot.send_message(user, 'Выберите турнир для участия', reply_markup=keyboard)
    
@bot.callback_query_handler(func=lambda call: True)
def buttons(call):
    user_id = call.message.chat.id
    user_name = call.message.chat.first_name                                 
    if call.message:
        if call.data == 'button1':
            if is_reg_open['chess'] == 0:
                bot.send_message(user_id, 'Регистрация Зарыта')
                bot.send_message(user_id, 'Если хотите выбрать другое направление нажмите /play')
                return
            if user_id not in users_chess:
                users_chess[user_id] = user_name
                bot.send_message(user_id, 'Вы записанны на шахматы, если захотите записатьться на другое направление, нажмите /play')
                return
            else:
                bot.send_message(user_id, 'Вы уже записанны на шахматы, если захотите записатьться на другое направление, нажмите /play')
                 
        if call.data == 'button2':
            if is_reg_open['tennis'] == 0:
                bot.send_message(user_id, 'Регистрация Зарыта')
                bot.send_message(user_id, 'Если хотите выбрать другое направление нажмите /play')
                return
            if user_id not in users_tennis:
                users_tennis[user_id] = user_name
                bot.send_message(user_id, 'Вы записанны на теннис, если захотите записатьться на другое направление, нажмите /play')
            else:
                bot.send_message(user_id, 'Вы уже записанны на теннис, если захотите записатьться на другое направление, нажмите /play')
                
        if call.data == 'button3':
            bot.send_message(user_id, 'Вы не участвуете, для записи нажмите /play')
            
bot.polling(none_stop=True)
