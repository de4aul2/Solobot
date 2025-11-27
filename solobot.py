from solodef import *


token = get_cfg()['Токен бота']
bot = telebot.TeleBot(token)
print('Бот запущен')


@bot.message_handler(content_types=['text'])
def message_handler(message):
    user_list = get_user_list()
    for i in user_list:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton('Пропустить', callback_data=f'Пропустить_{i[2]}')
        btn2 = types.InlineKeyboardButton('Заменить номер', callback_data=f'Заменить номер_{i[2]}')
        markup.row(btn1, btn2)
        bot.send_message(message.from_user.id, f'Имя: {i[0]}, номер: {i[1]}', reply_markup=markup)


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
