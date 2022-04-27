class Code:
    def __init__(self, num):
        self.num = num

    def process(self):
        for i in range(1, self.num + 1):
            number = int(input())
            if number == 88:
                print("Hello")
            elif number == 86:
                print("How are you?")
            elif number < 86 or number == 87:
                print("GREAT!")
            else:
                print("Bye.")


obj = Code(num=int(input()))
obj.process()
