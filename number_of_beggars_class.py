class BeggarNumber:
    def __init__(self, number_list, beggars):
        self.number_list = number_list
        self.beggars = beggars
        self.beggar_dict = {}
        self.sum_list = []

    def beggar_info(self):
        for beggar in range(1, self.beggars + 1):
            if beggar not in self.beggar_dict:
                self.beggar_dict[beggar] = []

    def beggar_data(self):
        beggar_count = 1
        for num in range(1, len(self.number_list) + 1):
            self.beggar_dict[beggar_count].append(self.number_list[num - 1])
            beggar_count += 1
            if beggar_count > self.beggars:
                beggar_count = 1

    def sum_result(self):
        for i in self.beggar_dict:
            if len(self.beggar_dict[i]) > 0:
                self.sum_list.append(sum(self.beggar_dict[i]))
            else:
                self.sum_list.append(0)
        print(self.sum_list)


obj = BeggarNumber(number_list=list(map(int, input().split(", "))), beggars=int(input()))
obj.beggar_info()
obj.beggar_data()
obj.sum_result()
