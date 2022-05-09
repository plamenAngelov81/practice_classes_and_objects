class WordFilter:
    def __init__(self, some_words):
        self.some_words = some_words
        self.even_words = []

    def process(self):
        for i in self.some_words:
            if len(i) % 2 == 0:
                self.even_words.append(i)

    def result(self):
        for i in self.even_words:
            print(i)


obj = WordFilter(some_words=input().split())
obj.process()
obj.result()
