import utils as util
import pandas as pd

INPUT = "data.csv"
OUTPUT = "result.txt"
2
# Чтение массива
try:
    data = pd.read_csv(INPUT, delimiter=",", dtype="float")
except Exception as e:
    exit(e)

theta0 = 0
theta1 = 0

# Сбор данных из файла
X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

message = "Введите пробег: \n"
str = input(message)

# Рассчет цены
try:
	value = float(str)
except Exception as e:
    exit(e)

try:
    f = open(OUTPUT)
    theta0 = float(f.readline())
    theta1 = float(f.readline())
except Exception as e:
    theta0 = 0
    theta1 = 0

if value < 0:
    exit("Невозможно спрогнозировать")
else:
    value = util.normalize(X, value)

cost = theta1 * value + theta0
if (cost > 0):
    cost = util.denormalize(Y, cost)

# Вывод цены
if (cost < 0):
    print ("Невозможно спрогнозировать")
else:
    print ("Прогнозная цена:")
    print (round(cost, 3))
