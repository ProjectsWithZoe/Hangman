import random

word_list = ['banana', 'grape', 'mango', 'mandarin', 'strawberry']
word = random.choice(word_list)

guess = input('Guess a letter')  

def check_guess (guess):
    guess.lower()
    if guess in word:
        print(f'Good guess!{guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_iput():
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

ask_for_iput()
