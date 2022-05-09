class Classification:
    def __init__(self, nums):
        self.nums = nums
        self.pos = []
        self.neg = []
        self.even = []
        self.odd = []

    def process(self):

        for num in self.nums:
            if num >= 0:
                self.pos.append(num)
            else:
                self.neg.append(num)

            if num % 2 == 0:
                self.even.append(num)
            else:
                self.odd.append(num)

        print(f"Positive: {', '.join(map(str, self.pos))}")
        print(f"Negative: {', '.join(map(str, self.neg))}")
        print(f"Even: {', '.join(map(str, self.even))}")
        print(f"Odd: {', '.join(map(str, self.odd))}")


obj = Classification(nums=list(map(int, input().split(", "))))
obj.process()
