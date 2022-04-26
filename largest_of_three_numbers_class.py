class BigNum:
    def __init__(self):
        self.largest_list = []

    def process(self):
        for i in range(1, 3 + 1):
            num = int(input())
            self.largest_list.append(num)

        self.largest_list = sorted(self.largest_list)
        largest_num = self.largest_list[-1]
        print(largest_num)


obj = BigNum()
obj.process()
