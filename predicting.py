import utils as util
import pandas as pd

INPUT = "data.csv"
OUTPUT = "result.txt"

# Чтение массива
try:
    data = pd.read_csv(INPUT, delimiter=",", dtype="float")
except Exception as e:
    exit(e)

# Сбор данных из файла
X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

message = "Введите пробег: \n"
str = input(message)

# Рассчет цены
try:
	value = util.normalize(X, float(str))
except Exception as e:
    exit(e)

try:
    f = open(OUTPUT)
    theta0 = float(f.readline())
    theta1 = float(f.readline())
except Exception as e:
	exit(e)

cost = theta1 * value + theta0
cost = util.denormalize(Y, cost)

# Вывод цены
if (value > 0 and cost > 0):
	print ("Прогнозная цена:")
	print (round(cost, 3))
else:
	print ("Невозможно спрогнозировать")
