class Age:
    def __init__(self, num):
        if num <= 14:
            print("drink toddy")
        elif 15 <= num <= 18:
            print("drink coke")
        elif 19 <= num <= 21:
            print("drink beer")
        else:
            print("drink whisky")


obj = Age(num=int(input()))
