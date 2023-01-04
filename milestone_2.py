import random

word_list = ['banana', 'grape', 'mango', 'mandarin', 'strawberry']
print(word_list)

word = random.choice(word_list)
print(word)

guess = input('Guess a letter')