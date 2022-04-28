class Profit:
    def __init__(self, group_size, days):

        coins = 0

        condition_5_day = False

        for day in range(1, days + 1):
            condition_5_day = False
            if day % 15 == 0:
                group_size += 5

            if day % 10 == 0:
                group_size -= 2

            if day % 3 == 0:
                coins -= group_size * 3
                condition_5_day = True

            if day % 5 == 0:
                coins += 20 * group_size

                if condition_5_day:
                    coins -= group_size * 2
            coins += 50 - group_size * 2

        coins_per_people = int(coins / group_size)

        print(f"{group_size} companions received {coins_per_people} coins each.")


obj = Profit(group_size=int(input()), days=int(input()))
