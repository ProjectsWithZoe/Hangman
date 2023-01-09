import random
from milestone_3 import word_list

class Hangman:
    def __init__(self,word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word_list = word_list
        

    def check_guess(self,guess):
        guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word.')        
        for i in range(len(self.word)):
            if self.word[i] == guess:
                self.word_guessed[i] = guess
        self.num_letters-=1
        

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter')
            if guess.isalpha() == False and len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
                
                

hangman = Hangman(word_list)
hangman.ask_for_input()