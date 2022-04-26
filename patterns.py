class Pattern:
    def __init__(self, num):
        for i in range(1, num + 1):
            print("*" * i)
        for j in range(1, num):
            print("*" * (num - 1))
            num -= 1


obj = Pattern(num=int(input()))
