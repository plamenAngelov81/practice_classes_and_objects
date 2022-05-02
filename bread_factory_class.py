class Factory:
    def __init__(self, events):
        self.events = events

    def process(self):
        energy = 100
        coins = 100

        close_condition = False

        for i in self.events:
            event = i.split("-")[0]
            value = int(i.split("-")[1])

            if event == "rest":
                if energy >= 100:
                    energy = 100
                    print("You gained 0 energy.")
                else:
                    energy += value
                    print(f"You gained {value} energy.")

                print(f"Current energy: {energy}.")

            elif event == "order":
                if energy >= 30:
                    print(f"You earned {value} coins.")
                    energy -= 30
                    coins += value
                else:
                    energy += 50
                    print("You had to rest!")
            else:
                if coins >= value:
                    print(f"You bought {event}.")
                    coins -= value
                else:
                    print(f"Closed! Cannot afford {event}.")
                    close_condition = True
                    break

        if not close_condition:
            print("Day completed!")
            print(f"Coins: {coins}")
            print(f"Energy: {energy}")


obj = Factory(events=input().split("|"))
obj.process()
