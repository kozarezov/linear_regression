import utils as util
import matplotlib.pyplot as plt
import pandas as pd

INPUT = "data.csv"
OUTPUT = "result.txt"

# https://baguzin.ru/wp/prostaya-linejnaya-regressiya/

# Чтение массива
try:
    data = pd.read_csv(INPUT, delimiter=",", dtype="float")
except Exception as e:
    exit(e)

if data.isnull().any().any() == True:
    exit("Не валидное значение в data.csv")

# Сбор данных из файла
X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

# Нормализация данных (уменьшение маштаба), для лучшего обучения
x = util.normalizeData(X)
y = util.normalizeData(Y)

# Инициализация переменных
m = len(X) # Количество наблюдений
theta0 = 0 # Коэффициент смещения
theta1 = 0 # Коэффициент наклона
learning_rate = 0.1 # Размер шага
iterations = 1500 # Количество итераций

# Инициализация визуального бекграунда
axes = plt.axes()
axes.grid()
axes.set_xlabel("Цена")
axes.set_ylabel("Пробег")
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
    
# Функция точности (метод наименьших квадратов)
def accuracy(theta0, theta1, x, y, m):
    accuracy = 0.0
    i = 0
    for i in range(0, m):
        estimatedPrice = theta0 + x[i] * theta1
        tmp = (y[i] - estimatedPrice) ** 2
        accuracy += tmp
    accuracy = accuracy / m
    return accuracy

# Градиентный спуск
def gradient_descent():
    tmp_theta0 = theta0
    tmp_theta1 = theta1
    cost = 1
    for it in range(0, iterations):
        sum1 = 0
        sum2 = 0
        for i in range(0, m):
            sum1 += ((tmp_theta1 * x[i] + tmp_theta0) - y[i])
            sum2 += (((tmp_theta1 * x[i] + tmp_theta0) - y[i]) * x[i])
        predicting_line(X, Y, tmp_theta1, tmp_theta0, it)
        tmp_theta0 = tmp_theta0 - (learning_rate * (sum1 / m))
        tmp_theta1 = tmp_theta1 - (learning_rate * (sum2 / m))
        old_cost = cost
        cost = accuracy(tmp_theta0, tmp_theta1, x, Y, m)
        delta = old_cost - cost
        axes.set_title('Accuracy: {}%'.format(int((1 - delta) * 100)))
        if (abs(delta) < 0.01):
            break
    return [tmp_theta0, tmp_theta1, it]

# Вывод итога на экран
[theta0, theta1, it] = gradient_descent()
[lx, ly] = predicting_line(X, Y, theta1, theta0, it)
axes.plot(lx, ly, color='red')
axes.text(X.min(), Y.min(), str(it), color = 'blue')
plt.show()

# Запись итога в файл
with open(OUTPUT, 'w') as f:
    f.write(str(theta0))
    f.write("\n")
    f.write(str(theta1))