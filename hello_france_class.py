class Hello:
    def __init__(self, data, budget):
        self.data = data
        self.budget = budget
        self.profit_list = []
        self.price_list = []

    def process(self):
        for i in self.data:
            item_price = i.split("->")
            item = item_price[0]
            price = float(item_price[1])
            if self.budget < price:
                pass
            else:
                if item == "Clothes" and price <= 50.00:
                    self.budget -= price
                    self.price_list.append(str(price))
                    new_price = price + (price * 0.4)
                    self.profit_list.append(f"{new_price:.2f}")
                elif item == "Shoes" and price <= 35.00:
                    self.budget -= price
                    self.price_list.append(str(price))
                    new_price = price + (price * 0.4)
                    self.profit_list.append(f"{new_price:.2f}")
                elif item == "Accessories" and price <= 20.50:
                    self.budget -= price
                    self.price_list.append(str(price))
                    new_price = price + (price * 0.4)
                    self.profit_list.append(f"{new_price:.2f}")
        print(" ".join(self.profit_list))

    def get_profit(self):
        profit_list = list(map(float, self.profit_list))
        price_list = list(map(float, self.price_list))
        profit = sum(profit_list) - sum(price_list)
        print(f"Profit: {profit:.2f}")

    def trip(self):
        total_list = list(map(float, self.profit_list))
        total_money = self.budget + sum(total_list)

        if total_money >= 150:
            print("Hello, France!")
        else:
            print("Not enough money.")


obj = Hello(data=input().split("|"), budget=float(input()))
obj.process()
obj.get_profit()
obj.trip()
