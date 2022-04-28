class Sleep:
    def __init__(self):
        event = input()
        coffee = 0
        while event != "END":

            if event.lower() == "coding":
                coffee += 1

            elif event.lower() == "dog" or event.lower() == "cat":
                coffee += 1

            elif event.lower() == "movie":
                coffee += 1

            if event.isupper():
                coffee += 1
            event = input()

        if coffee > 5:
            print("You need extra sleep")
        else:
            print(coffee)
