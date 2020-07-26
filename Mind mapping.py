import telebot


bot = telebot.TeleBot('')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('BrainStorming', 'Planning', 'Problem Solving', 'Info Presenting', 'Note Taking', 'Studying')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Group Discussion', 'Individual')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b> бот, ".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def question(message):
    if message.text.lower() == 'brainstorming':
        bot.send_message(message.chat.id, 'Ты выбрал BrainStorming', reply_markup=keyboard2)


bot.polling()