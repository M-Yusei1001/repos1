import matplotlib.pyplot as plt
import math

RANGE = 10
dx = 100

x = []
y = []

for num in range(0, dx):
    x.append(round((RANGE / dx) * num, 5))
for num in x:
    y.append(num*num)

#描画領域の確保
fig = plt.figure()

#図の追加
ax = fig.add_subplot(2,2,1)
ay = fig.add_subplot(2,2,3)

ay.scatter(y,x,marker="+",s=5)
ax.scatter(x, y, marker="+", s=5)
plt.show()
    