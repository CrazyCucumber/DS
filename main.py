import re
import pandas as pd
from scipy.spatial import distance

#открываем файл и запихиваем его в список
with open('sentences.txt', 'r') as fileSentences:
    dataSentences = list(fileSentences)


#приводим все буквы к нижнему регистру
#dataSentences имеет тип list, а его элементы тип str
dataSentencesLower = []
for i in range(len(dataSentences)):
    dataSentencesLower.append(dataSentences[i].lower())


#разбиваем на слова
dataWords = []
for line in dataSentencesLower:
    dataWords.append(re.split('[^a-z]', line))


#вычищаем пустые элементы
dataWordsCleared = [[] for i in range(len(dataWords))]
i = 0
for line in dataWords:
    for word in line:
        if word != '':
            dataWordsCleared[i].append(word)
    i = i + 1


#составляем список всех слов
dictWords = {}

i = 0
for line in dataWordsCleared:
    for word in line:
        if word not in dictWords:
            dictWords[word] = i
            i += 1


#создаем таблицу нужного нам размера и заполняем её нулями
frameWords = pd.DataFrame(dictWords, range(len(dataWordsCleared)))
row, col = frameWords.shape
for i in range(row):
    for j in range(col):
        frameWords.iloc[i, j] = 0


#заполняем данными нашу таблицу
for i in range(len(dataWordsCleared)):
    for word in dataWordsCleared[i]:
        frameWords.loc[i, word] += 1


#находим косинусное расстрояние и записываем в массив
distanceFromFirstSentence = []
for i in range(row):
    distanceFromFirstSentence.append(distance.cosine(frameWords.iloc[0], frameWords.iloc[i]))

distanceFromFirstSentenceCopy = list(distanceFromFirstSentence)
twoClosestValues = [[-1, 0], [-1, 0]]

distanceFromFirstSentenceCopy.remove(min(distanceFromFirstSentenceCopy))

for i in range(2):
    twoClosestValues[i][1] = min(distanceFromFirstSentenceCopy)
    for j in range(len(distanceFromFirstSentence)):
        if twoClosestValues[i][1] == distanceFromFirstSentence[j]:
            twoClosestValues[i][0] = j
    distanceFromFirstSentenceCopy.remove(min(distanceFromFirstSentenceCopy))

twoClosestValues = sorted(twoClosestValues)


#записываем все это в файл
with open('answer.txt', 'w') as fileAnswer:
    for i in range(len(twoClosestValues)):
        fileAnswer.write(str(twoClosestValues[i][0]) + ' ')
