class Message:
    def __init__(self, name):
        if name == "Johnny":
            print("Hello, my love!")
        else:
            print(f"Hello, {name}!")


obj = Message(name=input())
