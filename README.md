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

Finally the ask_for_input function is run to independently which is quicker than running the multiple lines of code previously.

Using OOP i created the Hangman class containing certain attributes such as word, word guessed, number of letters and lives, list of guesses and the word list.
2 functions were derived inside the hangman class and this were the check guess and ask for input functions. 

Check guess checked if the guess is in the word and if it was then the underscore was replaced by the letter and the number of unique letters to guess reduced by one.
If the guess wasnt in the word then the number of lives reduced by 1 and feedback was returned.

Ask for input checked if the code was invalid or already guessed and provided feedback.
If the code was valid then the check guess function would run and the guess is added to a list of already guessed letters.

Finally a play game function was created which created an instance of the Hangman game and ran as long as the number of lives was not 0 and the number of letters to guess was greater than 0.
If there were still lives and letters to guess the ask for input function would run.
Game is won if the number of lives is greater than 0 and the number of letters to guess is 0.

