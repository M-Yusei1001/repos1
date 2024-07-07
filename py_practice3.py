import matplotlib.pyplot as plt
import numpy as np
import math
import csv

MAX_RANGE = 1000
MAX_RANGE_2 = 5
MARKER_SIZE = 300 / (MAX_RANGE * 0.1)
if MARKER_SIZE < 1:
    MARKER_SIZE = 1
MARKER_TYPE = "+"

x = []
y = []

for value in range(0, MAX_RANGE):
    x.append(round((2 * math.pi) * ( value / MAX_RANGE ) * MAX_RANGE_2, 5))

for i in x:
    y.append(round(math.sin(i) + math.sin(i / MAX_RANGE_2), 5))               

with open("plot.csv", mode="w", encoding="utf-8-sig") as f:
    for i in range(0, len(x)):
        f.write(str(x[i]) + ", " + str(y[i]) + "\n") 

print("SUCCESSFULLY COMPLETE")
print("MARKER_SIZE > " + str(MARKER_SIZE))

x_read = []
y_read = []

with open("plot.csv", mode="r", encoding="utf-8-sig") as f:
    #.reader()メソッドにファイルオブジェクトfを渡す
    reader = csv.reader(f)

    for row in reader:
        #列番号（0始まり）を指定すると、その列に対応したデータを抜き出せる
        #取得したデータはstr型なので直す
        x_read.append(float(row[0]))
        y_read.append(float(row[1]))

#多項式の次数
d = 4

#回帰式の係数
w = np.polyfit(x_read, y_read, 2)

#多項式
func = np.poly1d(w)(x_read)

plt.scatter(x_read, y_read, marker=MARKER_TYPE, s=MARKER_SIZE , label="formula")
plt.plot(x_read, func, c="red", label="fitted")
plt.legend()
plt.grid()
plt.show()
