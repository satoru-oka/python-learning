# special method
class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'word.'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()

w1 = Word('T')
w2 = Word('T')
w3 = Word('text')

print(w3.text) # text
print(w1) # word.
print(w2) # word.
print(len(w1)) # 1
print(w1 + w2) # tt
print(w1 == w2) # true
