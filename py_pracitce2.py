#モノを買うプログラム

#商品の辞書
items = {"apple":100,"orange":200,"banana":150}

#所持金
money = 1000

print("あなたの所持金は" + str(money) + "円です")

#処理
for item in items:
    print("--------------------")
    print("購入する" + item + "の個数を入力してください:")
    item_input = input(">")

    price = items[item] * int(item_input)

    if price < money:
        print("購入金額は" + str(price) + "円です")
        money -= price

    elif price == money:
        print("購入金額は" + str(price) + "円です")
        print("所持金がなくなりました")
        money -= price
        break

    else:
        print("購入できませんでした")     

print("\n最終的な所持金は" + str(money) + "円です")           