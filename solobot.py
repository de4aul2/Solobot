from solodef import *


token = get_cfg()['Токен бота']
bot = telebot.TeleBot(token)
print('Бот запущен')


@bot.message_handler(content_types=['text'])
def message_handler(message):
    bot.send_message(message.chat.id, get_cfg()['Ключ API CRM системы'])



bot.delete_webhook()
bot.polling(none_stop=True, timeout=60)
