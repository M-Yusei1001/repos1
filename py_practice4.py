import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

path = "フォロワー数推移.csv"
df = pd.read_csv(path, encoding="utf-8-sig", parse_dates=["Date"])

print(df)

#描画領域の確保
fig = plt.figure()

#図の追加
ax = fig.add_subplot(1, 1, 1)

ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y\n%m-%d"))
ax.plot(df["Date"], df["Followers"])
plt.xticks(rotation = 90)
plt.grid()
plt.show()