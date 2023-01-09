# Hangman

This is a guessing game with a provided word list containing 5 fruits.
Using the random module, the computer chooses a particular fruit from the list randomly.
This chosen fruit then gets saved to a word variable.
The user then needs to guess single letters and they receive feedback on that input.
If the user doesn't enter a single letter but instead enters multiple letters or a number, they get feedback saying their input is invalid.
If they enter a single letter, they get feedback saying whether or not the letter is in the word.

Two functions were then created to make the tasks easier to understand. 
The check_guess function checks if the guessed letter is in the randomly chosen word.
The ask_for_input function is a while loop that checks if the entered input is valid and if it is it breaks out of the loop and runs the check_guess function.
If the entered input is invalid, the code continues in the infinite while loop and never reaches the check_guess function.
