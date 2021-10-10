import telebot
from functions_student import registration
from functions_teacher import data_check
from config import TOKEN
bot = telebot.TeleBot(TOKEN)


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Студент', 'Преподаватель')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nВыбери кто ты: студент или преподаватель', reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Студент':
        msg = bot.send_message(message.chat.id, f'{message.from_user.first_name}, пришли мне свой ID и ссылку на github'
                                                f'\nID и ссылку на github раздели запятой'
                                                f'\nВ ID укажи ФИО')
        bot.register_next_step_handler(msg, student_register)
    elif message.text == 'Преподаватель':
        msg = bot.send_message(message.chat.id, f'{message.from_user.first_name}, список тех, кто прикрепился: \n')
        bot.register_next_step_handler(msg, teacher_next_step)
def student_register(message):
    registration(message)
def teacher_next_step(message):
    data_check(message)



if __name__ == '__main__':
     bot.polling(none_stop=True)
