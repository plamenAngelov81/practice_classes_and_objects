class Invert:

    def __init__(self):
        self.invert_nums = []

    def process(self, numbers):
        for i in numbers:
            if i > 0:
                self.invert_nums.append(-i)
            else:
                self.invert_nums.append(abs(i))

        return self.invert_nums


obj = Invert()
obj.process(numbers=list(map(int, input().split())))
print(obj.invert_nums)
