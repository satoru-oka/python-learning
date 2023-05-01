weekly = ['Mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# change_words(weekly, sample_func)
# sample_func = lambda word: word.capitalize()
change_words(weekly, lambda word: word.capitalize())
change_words(weekly, lambda word: word.lower())