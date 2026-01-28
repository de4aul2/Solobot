from solodef import *


token = get_cfg()['Токен бота']
bot = telebot.TeleBot(token)
print('Бот запущен')


@bot.message_handler(content_types=['text'])
def message_handler(message):
    if check_db():
        bot.send_message(message.chat.id, "Файл базы данных существует.")
    else:
        bot.send_message(message.chat.id, "Файл БД не существует.\nФайл базы данных создан.")


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    data_parts = callback.data.split('_')
    action = data_parts[0]
    userid = data_parts[1] if len(data_parts) > 1 else None
    if action == 'Пропустить':
        print(f'Пропустить пользователя: {userid}')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif action == 'Заменить номер':
        print(f'Заменить номер для пользователя: {userid}')
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        replace_number(userid)


bot.delete_webhook()
bot.polling(none_stop=True, timeout=60)
