import numpy as np
from scipy import linalg
import matplotlib.pylab as plt
from math import sin, exp


#задаём функцию и y и x координаты
def func(x):
    return sin(x / 5.) * exp(x / 10.) + 5. * exp(-x / 2.)
arrCoordinates = np.arange(1., 15.1, 0.1)
arrFunction = np.array([func(coordinate) for coordinate in arrCoordinates])


#сформировать СЛАУ для многочлена первой степени, который должен совпадать
#с функцией в точках 1 и 15
arrCoord1 = np.array([1, 15])
N = 2
arrA1 = np.empty((0, N))
for i in range(N):
    arrA1Line = list()
    for j in range(N):
        arrA1Line.append(arrCoord1[i] ** j)
    arrA1 = np.append(arrA1, np.array([arrA1Line]), axis = 0)

arrB1 = np.array([func(coordinate) for coordinate in arrCoord1])

arrX1 = linalg.solve(arrA1, arrB1)

def func1(x): return arrX1[0] + arrX1[1] * x
arrFunc1 = np.array([func1(coordinate) for coordinate in arrCoordinates])

plt.plot(arrCoordinates, arrFunction, arrCoordinates, arrFunc1)
plt.show()


#многочлен второй степени в точках 1, 8, 15
arrCoord2 = np.array([1, 8, 15])
N = 3
arrA2 = np.empty((0, N))
for i in range(N):
    arrA2Line = list()
    for j in range(N):
        arrA2Line.append(arrCoord2[i] ** j)
    arrA2 = np.append(arrA2, np.array([arrA2Line]), axis=0)

arrB2 = np.array([func(coordinate) for coordinate in arrCoord2])

arrX2 = linalg.solve(arrA2, arrB2)

def func2(x): return arrX2[0] + arrX2[1] * x + arrX2[2] * (x ** 2)
arrFunc2 = np.array([func2(coordinate) for coordinate in arrCoordinates])

plt.plot(arrCoordinates, arrFunction, arrCoordinates, arrFunc1, arrCoordinates, arrFunc2)
plt.show()


#многочлен 3 степени в точках 1, 4, 10, 15
arrCoord3 = np.array([1, 4, 10, 15])
N = 4
arrA3 = np.empty((0, N))
for i in range(N):
    arrA3Line = list()
    for j in range(N):
        arrA3Line.append(arrCoord3[i] ** j)
    arrA3 = np.append(arrA3, np.array([arrA3Line]), axis=0)

arrB3 = np.array([func(coordinate) for coordinate in arrCoord3])

arrX3 = linalg.solve(arrA3, arrB3)

def func3(x): return arrX3[0] + arrX3[1] * x + arrX3[2] * (x ** 2) + arrX3[3] * (x ** 3)
arrFunc3 = np.array([func3(coordinate) for coordinate in arrCoordinates])

plt.plot(arrCoordinates, arrFunction, arrCoordinates, arrFunc1, arrCoordinates, arrFunc2, arrCoordinates, arrFunc3)
plt.show()


#запись в файл
with open('answer2.txt', 'w') as fileAnswer:
    for item in arrX3:
        fileAnswer.write(str(item) + ' ')
