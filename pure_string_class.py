class Pure:
    def __init__(self, num):

        for i in range(1, num + 1):
            data = input()
            if "_" in data or "." in data or "," in data:
                print(f"{data} is not pure!")
            else:
                print(f"{data} is pure.")


obj = Pure(num=int(input()))
