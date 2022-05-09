class Group:
    def __init__(self, some_numbers):
        self.some_numbers = some_numbers

    def process(self):
        group = 10

        while len(self.some_numbers) > 0:
            group_list = []

            for i in self.some_numbers:
                if i <= group:
                    group_list.append(i)

            for x in group_list:
                self.some_numbers.remove(x)

            print(f"Group of {group}'s: {group_list}")
            group += 10


obj = Group(some_numbers=list(map(int, input().split(", "))))
obj.process()
