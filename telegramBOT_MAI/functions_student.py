# from datetime import datetime
import telebot
from config import TOKEN
bot = telebot.TeleBot(TOKEN)
#
#
# def transformation_data():
#     current_datetime = datetime.now()
#     pos = str(current_datetime).rfind('.')
#     current_datetime = ' Сделал последний commit: ' + str(current_datetime)[ : pos] + '\n'
#     return str(current_datetime)
#
#
# def add_to_file(ID, Link):
#     with open("Github Data", "a") as file:
#         file.write(ID)
#         file.write(Link)
#         file.write(transformation_data())
#
#
# def read_file_in_array_and_transformation():
#     lines_array = []
#     with open("Github Data", "r") as file:
#         lines = file.read().splitlines()
#     for line in lines:
#         pos = line.find(' h')
#         lines_array.append(line[:pos])
#     return lines_array
#
#
# def delete_string_from_file(number_of_string):
#     i = 0
#     with open("Github Data", "r") as file:
#         lines = file.read().splitlines()
#     with open("Github Data", "w") as file:
#         for line in lines:
#             if i != number_of_string:
#                 i += 1
#                 ln = line + '\n'
#                 file.write(ln)
#
#
#
# def registration(message):
#     buffer = message.text
#     ID = ' '
#     Link = ' '
#
#     if buffer.find(',') != -1:
#         comma_position = buffer.find(',')
#         ID = buffer[: comma_position]
#         Link = buffer[comma_position + 1:]
#     elif buffer.find(',') == -1 and buffer.find('http') != -1:
#         href_position = buffer.find('http')
#         ID = message.from_user
#         Link = buffer[href_position + 1:]
#     elif buffer.find(',') == -1 and buffer.find('http') == -1:
#         return bot.send_message(message.chat.id,
#                                 f'{message.from_user.first_name}, ты не ввёл ссылку, попробуй ещё раз')
#
#     number_of_string = -1
#     for i in range(0, len(read_file_in_array_and_transformation())):
#         if ID == read_file_in_array_and_transformation()[i]:
#             number_of_string = i
#     if number_of_string == -1:
#         add_to_file(ID, Link)
#     else:
#         delete_string_from_file(number_of_string)
#         add_to_file(ID, Link)
#
#     return bot.send_message(message.chat.id,
#                             f'{message.from_user.first_name}, ты записан!')
#
def registration(message):
    lst = message.text.split(', ')
    if len(lst) != 5:
        bot.send_message(message.chat.id,
                                     f'{message.from_user.first_name}, не правильный формат сообщения')
        return -1
    name = lst[0]
    group = lst[1]
    task = lst[2]
    variant = lst[3]
    git = lst[4]

    group_lst = ('212Б', '221Б', '214Б')
    if group not in group_lst:
        bot.send_message(message.chat.id,
                         f'{message.from_user.first_name}, не правильный формат сообщения')
        return -2

    if int(task) < 1 or int(task) > 5:
        print('Неправильный номер задания')
        print('Возможный номер задания от 1 до 5')
        return -3

    if int(variant) < 1 or int(variant) > 5:
        print('Неправильный номер варианта')
        print('Возможный номер номер варианта от 1 до 5')
        return -4

    if 'github.com/' not in git:
        print('Некорркетная ссылка')
        return -5
