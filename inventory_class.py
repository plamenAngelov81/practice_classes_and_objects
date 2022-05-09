class Inventory:
    def __init__(self, items):
        self.items = items

        command = input().split(" - ")
        while True:
            if command[0] == "Craft!":
                break

            if command[0] == "Collect":
                collect_item = command[1]
                if collect_item not in self.items:
                    self.items.append(collect_item)

            elif command[0] == "Drop":
                drop_item = command[1]
                if drop_item in self.items:
                    self.items.remove(drop_item)

            elif command[0] == "Combine Items":
                old_item = command[1].split(":")[0]
                new_item = command[1].split(":")[1]
                if old_item in self.items:
                    self.items.insert(self.items.index(old_item) + 1, new_item)

            elif command[0] == "Renew":
                renew_item = command[1]
                if renew_item in self.items:
                    self.items.remove(renew_item)
                    self.items.append(renew_item)

            command = input().split(" - ")

        print(", ".join(self.items))


obj = Inventory(items=input().split(", "))
