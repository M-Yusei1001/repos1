import time
import datetime as dt

for i in range(0, 10):
    now = dt.datetime.now()
    print("現在の日時：", now.strftime("%Y年%m月%d日 %H時%M分%S秒"))
    time.sleep(1)

