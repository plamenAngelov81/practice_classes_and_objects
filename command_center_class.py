class CommandCenter:
    def __init__(self, numbers):
        self.numbers = numbers

    def process(self):
        command_data = input().split()
        command_count = 0
        while True:
            if command_data[0] == "end":
                break

            if command_data[0] == "swap":
                index_1 = int(command_data[1])
                index_2 = int(command_data[2])
                if 0 <= index_1 <= len(self.numbers) - 1 and 0 <= index_2 <= len(self.numbers) - 1:
                    self.numbers[index_1], self.numbers[index_2] = self.numbers[index_2], self.numbers[index_1]
                    print(self.numbers)
                    command_count += 1
                else:
                    print(self.numbers)
                    command_count += 1
            elif command_data[0] == "enumerate_list":
                enumerate_list = []
                for i in range(len(self.numbers)):
                    tuple_result = (i, self.numbers[i])
                    enumerate_list.append(tuple_result)
                print(enumerate_list)
                command_count += 1
            elif command_data[0] == "max":
                print(max(self.numbers))
                command_count += 1
            elif command_data[0] == "min":
                print(min(self.numbers))
                command_count += 1
            elif command_data[0] == "get_divisible":
                divider = int(command_data[2])
                result_list = []
                for i in self.numbers:
                    if i % divider == 0:
                        result_list.append(i)
                print(result_list)
                command_count += 1
            command_data = input().split()

        print(command_count)


obj = CommandCenter(numbers=list(map(int, input().split())))
obj.process()
