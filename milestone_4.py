import random

class Hangman:
    def __init__(self,word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for i in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []
        

