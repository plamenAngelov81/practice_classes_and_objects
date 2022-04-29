class Shuffle:
    def __init__(self, card_list, num):
        self.num = num
        self.card_list = card_list

        limit = int(len(self.card_list) / 2)

        for i in range(1, self.num + 1):
            first_part = self.card_list[:limit]
            second_part = self.card_list[limit:]
            new_list = []
            for j in range(limit):
                new_list.append(first_part[j])
                new_list.append(second_part[j])
            self.card_list = new_list

        print(self.card_list)


obj = Shuffle(card_list=input().split(), num=int(input()))
