class CharSum:
    def __init__(self, num):
        char_sum = 0
        for i in range(1, num + 1):
            char = input()
            char_sum += ord(char)

        print(char_sum)


obj = CharSum(num=int(input()))

