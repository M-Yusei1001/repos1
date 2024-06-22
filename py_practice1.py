import utility as util

print("何個商品を登録しますか？")
num = int(input(">"))

items = []

for i in range(0, num):
    print("----------------")
    print("情報を入力してください")
    print("商品名,価格,カロリー\tの順で入力")
    data = input(">").split(",")

    items.append(util.MenuItem(data[0], data[1], data[2]))

for i in range(0, num):
    print("----------------")
    print("No. " + str(i + 1))
    items[i].info()

print("----------------")
print("何個購入しますか？")
total_price = 0

for i in range(0, num):
    quantity = int(input(items[i].name + ">"))

    if util.check_zero(quantity):
        total_price += items[i].get_total_price(quantity)
    else:
        print("入力が不正です")       


print("----------------")
print("合計" + str(total_price) + "円です")    