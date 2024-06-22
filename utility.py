class MenuItem:
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = price
        self.calorie = calorie

    def info(self):
        print("----------------")
        print("商品名：" + self.name)
        print("価格：" + str(self.price))
        print("カロリー：" + str(self.calorie))

    def get_total_price(self, num):
        return self.price * num  
