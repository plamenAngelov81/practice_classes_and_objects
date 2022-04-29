class EasterGift:
    def __init__(self, gift_list):
        self.gift_list = gift_list

    def commands(self):
        gift_data = input().split()
        while True:
            if gift_data[0] == "No":
                break

            if gift_data[0] == "OutOfStock":
                replace_item = gift_data[1]
                for i in range(len(self.gift_list)):
                    if self.gift_list[i] == replace_item:
                        self.gift_list[i] = "None"

            elif gift_data[0] == "Required":
                required_item = gift_data[1]
                index = int(gift_data[2])
                if 0 <= index <= len(self.gift_list) - 1:
                    self.gift_list[index] = required_item

            elif gift_data[0] == "JustInCase":
                new_item = gift_data[1]
                self.gift_list[-1] = new_item

            gift_data = input().split()

        final_list = [x for x in self.gift_list if x != "None"]
        print(" ".join(final_list))
        # print(" ".join(x for x in gift_list if x != "None"))


obj = EasterGift(gift_list=input().split())
obj.commands()
