class Orders:
    def __init__(self, orders):
        total = 0

        for order in range(1, orders + 1):
            price_per_capsule = float(input())
            days = int(input())
            capsules_count = int(input())
            if 1 <= days <= 31 and 1 <= capsules_count <= 2000 and 0.01 <= price_per_capsule <= 100.00:
                price = price_per_capsule * days * capsules_count
                print(f"The price for the coffee is: ${price:.2f}")
                total += price
        print(f"Total: ${total:.2f}")


obj = Orders(orders=int(input()))
