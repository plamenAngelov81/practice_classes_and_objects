class MaxMulty:
    def __init__(self, number, limit):

        result = []

        for i in range(number, limit + 1):
            if i % number == 0:
                result.append(i)

        print(result[-1])


obj = MaxMulty(number=int(input()), limit=int(input()))
