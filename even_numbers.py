class EvenNumbers:
    def __init__(self, n):
        self.n = n

    def process(self):
        even_num = True
        for i in range(1, self.n + 1):
            num = int(input())
            if num % 2 != 0:
                print(f"{num} is odd!")
                even_num = False
                break

        if even_num:
            print("All numbers are even.")


obj = EvenNumbers(n=int(input()))
obj.process()
