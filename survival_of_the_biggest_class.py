class BiggestNum:
    def __init__(self, numbers, n):
        self.numbers = numbers
        self.n = n
        for i in range(self.n):
            current_num = min(self.numbers)
            self.numbers.remove(current_num)
        print(", ".join(map(str, self.numbers)))


obj = BiggestNum(numbers=list(map(int, input().split())), n=int(input()))
