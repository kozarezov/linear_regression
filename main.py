import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

""" https://github.com/SpenderJ/Linear_Regression/blob/master/training.py """

INPUT = "data.csv"

try:
    data = pd.read_csv(INPUT, delimiter=",", dtype="float")
except Exception as e:
    exit(e)

X = data.iloc[0:len(data), 0]
Y = data.iloc[0:len(data), 1]

max_Y = max(Y)
min_Y = min(Y)

max_X = max(X)
min_X = min(X)

axes = plt.axes()
axes.grid()
