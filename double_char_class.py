class DoubleChar:
    def __init__(self):
        some_string = input()

        while True:
            if some_string == "End":
                break
            if some_string != "SoftUni":
                letters = ""
                for i in some_string:
                    letters += i * 2
                print(letters)
            some_string = input()


obj = DoubleChar()
