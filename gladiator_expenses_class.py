class Gladiator:
    def __init__(self, lost_fights, helmet_price, sword_price, shield_price, armor_price):
        aureus = 0
        broken_shield = 0

        for i in range(1, lost_fights + 1):

            if i % 2 == 0:
                aureus += helmet_price
            if i % 3 == 0:
                aureus += sword_price
                if i % 2 == 0:
                    aureus += shield_price
                    broken_shield += 1
                    if broken_shield == 2:
                        aureus += armor_price
                        broken_shield = 0
        print(f"Gladiator expenses: {aureus:.2f} aureus")


obj = Gladiator(lost_fights=int(input()), helmet_price=float(input()), sword_price=float(input()),
                shield_price=float(input()), armor_price=float(input()))
