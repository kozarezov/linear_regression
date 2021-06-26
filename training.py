import time
import utils as util
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

INPUT = "data.csv"

# Чтение массива
try:
    data = pd.read_csv(INPUT, delimiter=",", dtype="float")
except Exception as e:
    exit(e)

# Инициализация X и Y
X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

# Нормализация данных (уменьшение маштаба), для лучшего обучения
x = util.normalizeData(X)
y = util.normalizeData(Y)

# Инициализация переменных
m = len(X) # Количество наблюдений
theta0 = 0
theta1 = 0
learning_rate = 0.1 # Размер шага
iterations = 1000 # Количество итераций

# Инициализация визуального бекграунда
axes = plt.axes()
axes.grid()
plt.scatter(X, Y)

# Функция для визуализации линии
def predicting_line(X, Y, theta1, theta0, it):
    lx = [X.min(), X.max()]
    ly = []
    for j in lx:
        j = theta1 * util.normalize(X, j) + theta0
        price = util.denormalize(Y, j)
        ly.append(price)
    [ln] = axes.plot(lx, ly, color='red')
    lt = axes.text(X.min(), Y.min(), str(it), color = 'blue')
    plt.draw()
    plt.pause(0.0000000000000000000001)
    ln.remove()
    lt.remove()
    return(lx, ly)

# Градиентный спуск
def gradient_descent():
    tmp_theta0 = theta0
    tmp_theta1 = theta1
    for it in range(0, iterations):
        sum1 = 0
        sum2 = 0
        for i in range(0, m):
            sum1 += ((tmp_theta1 * x[i] + tmp_theta0) - y[i])
            sum2 += (((tmp_theta1 * x[i] + tmp_theta0) - y[i]) * x[i])
        predicting_line(X, Y, tmp_theta1, tmp_theta0, it)
        tmp_theta0 = tmp_theta0 - (learning_rate * (sum1 / m))
        tmp_theta1 = tmp_theta1 - (learning_rate * (sum2 / m))
    return [tmp_theta0, tmp_theta1]

[theta0, theta1] = gradient_descent()

[lx, ly] = predicting_line(X, Y, theta1, theta0, 1000)
axes.plot(lx, ly, color='red')
axes.text(X.min(), Y.min(), str(iterations), color = 'blue')
plt.show()