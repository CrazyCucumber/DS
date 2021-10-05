import re
import numpy as np
from scipy.spatial import distance


#открываем файл
file1 = open("sentences.txt", "r")


#считываем файл и приводим все буквы к нижнему регистру
lines = file1.read().lower()
pr = lines.split('.\n')


#загоняем все слова в список и в цикле for удаляем пустые элементы
words = re.split('[^a-z]', lines)
for element in words:
    if element == '':
        words.remove(element)


#создаём словарь, в котором будем вести подсчёт слов
#с помощью цикла пробегаю по каждому элементу и если его нет в славаре, то записываю туда
#где число элементов нахожу с помощью метода списка
count = {}
for element in words:
    if count.get(element) == None:
        count.update({element: words.count(element)})


#делаем буфер и создаем единичную матрицу размера 22 на 255(какая матрица не важно, сейчас важен только размер)
#далее каждую строку, полученную перебором списка, закидываем в буффер, преобразовывая в список
#далее берем по слову из словаря и находим количество его вхождений в строку и записываем это в
#нужную ячейку в матрице
buffer = ' '
matrix = np.eye(22, 255)
for i in range(0, 22):
    j = 0
    buffer = pr[i].split(' ')
    for key in count.keys():
        k = buffer.count(key) + buffer.count(key + ',') + buffer.count(key + '.')
        matrix[i][j] = k
        j += 1


#нахождение косинусного расстояния и выбор
#двух максимально похожих
value, min1, min2 = 0, 2, 2
sentenc1, sentenc2 = 0, 0
for i in range(1, 22):
    value = distance.cosine(matrix[0][:], matrix[i][:])
    if value < min1:
        min2 = min1
        sentenc2 = sentenc1
        min1 = value
        sentenc1 = i
    elif value < min2:
        min2 = value
        sentenc2 = i


#запись в данных в файл
strng = str(sentenc2) + ' ' + str(sentenc1)
file_answer = open("answer.txt", "w")
file_answer.write(strng)
