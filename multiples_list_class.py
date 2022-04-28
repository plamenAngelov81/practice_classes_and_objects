class NumList:

    def __init__(self):
        self.multiply_list = []

    def multiply_nums(self, factor, count):
        for i in range(1, count + 1):
            result = i * factor
            self.multiply_list.append(result)
        return self.multiply_list


obj = NumList()
obj.multiply_nums(factor=int(input()), count=int(input()))
print(obj.multiply_list)
