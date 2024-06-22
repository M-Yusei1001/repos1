class MenuItem:
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = int(price)
        self.calorie = int(calorie)

    def info(self):
        print("商品名：" + self.name)
        print("価格：" + str(self.price) + " 円")
        print("カロリー：" + str(self.calorie) + " kcal")

    def get_total_price(self, num):
        if num >= 3:
            return round(self.price * 0.9 * num)
        else:
            return self.price * num  

def check_zero(num):
    if num > 0:
        return True
    else:
        return False