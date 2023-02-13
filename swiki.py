import telebot
import wikipedia
import config

bot=telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Поиск')
    bot.send_message(message.chat.id, 'Привет! Данный телеграм-бот ищет термины в википедии. Будем рады тебе помочь', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def search(message):
    if message.text =='Поиск':

        messid = message.chat.id
        msgsearch = bot.send_message(messid, 'Введите поле для поиска')
        bot.register_next_step_handler(msgsearch, step_set_search)


def step_set_search(message):
    try:

        usersearch = message.text
        wikipedia.set_lang("ru")
        bot.send_message(message.chat.id, wikipedia.summary(str(usersearch)), parse_mode='Markdown')
    except:
        bot.send_message(message.chat.id, "такого слова нет.Поищи еще раз", parse_mode='Markdown')




bot.polling()