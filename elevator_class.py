class Elevator:
    def __init__(self, people, capacity):
        turns = 0
        while True:
            people -= capacity
            turns += 1
            if people <= 0:
                break
        print(turns)


obj = Elevator(people=int(input()), capacity=int(input()))
