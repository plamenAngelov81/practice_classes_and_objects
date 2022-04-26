class Between:
    def __init__(self):
        while True:
            num = float(input())
            if 1 <= num <= 100:
                print(f"The number {num} is between 1 and 100")
                break


obj = Between()
