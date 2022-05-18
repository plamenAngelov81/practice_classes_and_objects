class FashionBoutique:
    def __init__(self, clothes, rack_capacity):
        self.clothes = clothes
        self.rack_capacity = rack_capacity

    def process(self):
        rack_counter = 1
        current_rack_capacity = self.rack_capacity

        while self.clothes:
            current_item_capacity = self.clothes[-1]
            if current_rack_capacity >= current_item_capacity:
                current_rack_capacity -= current_item_capacity
                self.clothes.pop()
            else:
                rack_counter += 1
                current_rack_capacity = self.rack_capacity
                current_rack_capacity -= current_item_capacity
                self.clothes.pop()
        print(rack_counter)


obj = FashionBoutique(clothes=list(map(int, input().split())), rack_capacity=int(input()))
obj.process()
