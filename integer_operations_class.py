class IntegerOperations:
    def __init__(self, num_1, num_2, num_3, num_4):
        result = int((num_1 + num_2) / num_3) * num_4
        print(result)


obj = IntegerOperations(num_1=int(input()), num_2=int(input()), num_3=int(input()), num_4=int(input()))
