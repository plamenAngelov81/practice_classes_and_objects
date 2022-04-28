class Print:
    def __init__(self, a, b):
        print(" ".join(chr(x) for x in range(a, b + 1)))

        #for i in range(a, b + 1):
            #print(chr(i), end=" ")


obj = Print(a=int(input()), b=int(input()))
