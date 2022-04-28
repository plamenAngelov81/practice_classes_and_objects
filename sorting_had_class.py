class Hogwards:
    def __init__(self):
        self.name_list = []

    def sort_process(self):
        name = input()
        while True:
            if name == "Welcome!":
                break
            if name == "Voldemort":
                self.name_list.append(name)
                break
            else:
                self.name_list.append(name)
            name = input()

    def result(self):
        condition = True
        for i in self.name_list:
            if i == "Voldemort":
                print("You must not speak of that name!")
                condition = False
                break
            else:
                if len(i) < 5:
                    print(f"{i} goes to Gryffindor.")
                elif len(i) == 5:
                    print(f"{i} goes to Slytherin.")
                elif len(i) == 6:
                    print(f"{i} goes to Ravenclaw.")
                elif len(i) > 6:
                    print(f"{i} goes to Hufflepuff.")

        if condition:
            print("Welcome to Hogwarts.")


obj = Hogwards()
obj.sort_process()
obj.result()
