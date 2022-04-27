class EasterBread:

    def __init__(self, budget: float, flour_price: float, bread_price, breads_counter, colored_eggs):
        self.breads_counter = breads_counter
        self.colored_eggs = colored_eggs
        self.budget = budget
        self.flour_price = flour_price
        self.bread_price = bread_price

    def prices(self):
        egg_pack_price = self.flour_price * 0.75
        milk_price = self.flour_price + (self.flour_price * 0.25)
        milk_price_per_bread = milk_price * 0.25

        self.bread_price = egg_pack_price + self.flour_price + milk_price_per_bread

    def eggs_bread(self):

        while True:
            if self.budget >= self.bread_price:
                self.breads_counter += 1
                self.colored_eggs += 3
                self.budget -= self.bread_price
                if self.breads_counter % 3 == 0:
                    egg_lost = self.breads_counter - 2
                    self.colored_eggs -= egg_lost

            if self.budget < self.bread_price:
                break

    def __repr__(self):
        result = f"You made {self.breads_counter} loaves of Easter bread! Now you have {self.colored_eggs} eggs and " \
                 f"{self.budget:.2f}BGN left."
        return result


eggs_bread_count = EasterBread(budget=float(input()), flour_price=float(input()), bread_price=0, breads_counter=0,
                               colored_eggs=0)
eggs_bread_count.prices()
eggs_bread_count.eggs_bread()
print(eggs_bread_count)
