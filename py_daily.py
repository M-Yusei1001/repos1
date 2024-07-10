import matplotlib.pyplot as plt
import math

RANGE = 100
MULTIPY = 100
MARKER_SIZE = 5

x = []
ya = []
yb = []
yc = []

for i in range(0, RANGE + 1):
    x.append(round((1/MULTIPY)*i, 5))

for i in x:
    a = round(math.sin(2 * i), 5)
    b = round(math.exp(-i), 5)
    c = a * b

    ya.append(a)
    yb.append(b)
    yc.append(c)

#描画領域の用意
fig = plt.figure()

#図の用意
ax = fig.add_subplot(1,1,1)

ax.scatter(x, ya, marker="+", s = MARKER_SIZE, label="sin(2x)")
ax.scatter(x, yb, marker="+", s = MARKER_SIZE, label="exp(-x)")
ax.scatter(x, yc, marker="+", s = MARKER_SIZE, label="exp(-x)*sin(2x)")

ax.legend()
plt.grid()
plt.show()