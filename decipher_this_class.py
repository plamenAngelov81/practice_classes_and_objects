class Decipher:
    def __init__(self, code):
        self.code = code
        self.decoded_string = []

    def process(self):
        for i in self.code:
            word_list = list(i)
            num = ""
            while word_list[0] in "1234567890":
                num += word_list[0]
                word_list.pop(0)
            num_to_str = chr(int(num))
            word_list.insert(0, num_to_str)

            word_list[1], word_list[-1] = word_list[-1], word_list[1]
            self.decoded_string += ["".join(word_list)]
        for j in self.decoded_string:
            print(j, end=" ")


obj = Decipher(code=input().split(" "))
obj.process()
