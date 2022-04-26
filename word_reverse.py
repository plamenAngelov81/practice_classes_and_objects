class ReversedWord:
    def __init__(self, word):
        self.word = word

    def process(self):
        print(self.word[::-1])


obj = ReversedWord(word=input())
obj.process()
