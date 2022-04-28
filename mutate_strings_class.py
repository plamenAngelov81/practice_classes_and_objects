class MutateStrings:
    def __init__(self, first_word, second_word):
        self.first_word = first_word
        self.second_word = second_word
        
    def process(self):
        for i in range(len(self.first_word)):
            if self.first_word[i] != self.second_word[i]:
                replacement = self.second_word[i]
                word = self.first_word[0:i] + replacement + self.first_word[i + 1:]
                self.first_word = word
                print(self.first_word)


obj = MutateStrings(first_word=input(), second_word=input())
obj.process()
