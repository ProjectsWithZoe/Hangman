import random

word_list = ['banana', 'grape', 'mango', 'mandarin', 'strawberry']
word = random.choice(word_list)
guess = input('Guess a letter')

while True:
    guess = input('Guess a letter')
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

for letter in word:
    if guess == letter:
        print(f'Good guess!')
    else:
        print('Sorry, {guess} is not in the word. Try again.')
