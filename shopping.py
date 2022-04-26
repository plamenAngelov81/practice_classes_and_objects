class Shopping:
    def __init__(self):

        budget = int(input())
        command = input()

        while True:
            if command == "End":
                print("You bought everything needed.")
                break
            price = int(command)
            if price > budget:
                print("You went in overdraft!")
                break
            budget -= price
            command = input()


obj = Shopping()
