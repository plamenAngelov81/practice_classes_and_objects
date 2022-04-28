class Tank:
    def __init__(self, num):

        total_litters = 0
        for i in range(1, num + 1):
            current_litters = int(input())
            diff = 255 - total_litters
            if current_litters > diff:
                print("Insufficient capacity!")
            else:
                total_litters += current_litters

        print(f"{total_litters}")


obj = Tank(num=int(input()))
