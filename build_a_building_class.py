class Building:
    def __init__(self, needed_money, start_capital, investors):
        self.needed_money = needed_money
        self.start_capital = start_capital
        self.investors = investors

#
    def process(self):
        build_condition = False

        for i in range(1, self.investors + 1):
            investor_money = float(input())
            self.start_capital += investor_money
            print(f"Investor {i} gave us {investor_money:.2f}.")
            if self.start_capital >= self.needed_money:
                build_condition = True
                break

        if build_condition:
            diff_1 = self.start_capital - self.needed_money
            print(f"We will manage to build it. Start now! Extra money - {diff_1:.2f}.")
        else:
            dif_2 = self.needed_money - self.start_capital
            print(f"Project can not start. We need {dif_2:.2f} more.")


obj = Building(needed_money=float(input()), start_capital=float(input()), investors=int(input()))
obj.process()
