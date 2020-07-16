import random


def print_gallows(guesses, word):
    """
    Function to print the gallows in console, if not necessary if we have an other interface
    :param guesses: to get the guesses of the user
    :param word: correct word to guess
    """
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	_|")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	_|_")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	_|_")
        print("|	 |")
        print("|	_|")
        print("|________")
    elif guesses == 6:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	_|_")
        print("|	 |")
        print("|	_|_ ")
        print("|________")
        print("The word was %s." % word)
        print("YOU LOSE! TRY AGAIN!")
        print("Would you like to play again, type [y] for yes or [n] for no?")
        again = str(input())
        again = again.lower()
        if again == "y":
            run_hangman()
        return


def get_a_word():
    """
    Function to get a word from a txt with a list of words
    A txt file is used to change the list of words easy whenever we want
    Maybe others format to use could be a CSV or get words from a DB
    return a selected randomized word
    """
    # read from file and get the words
    file = open('hangman_words.txt')
    words = file.readlines()
    selected_word = 'ha'  # by default a simple word
    while len(selected_word) < 5:  # makes sure word is at least 5 letters long
        # pick up an other random word while length is less than 5
        # formatted the word
        selected_word = random.choice(words)
        selected_word = str(selected_word).strip('[]')
        selected_word = str(selected_word).strip("''")
        selected_word = str(selected_word).strip("\n")
        selected_word = str(selected_word).strip("\r")
    selected_word = selected_word.lower()
    return selected_word


def run_hangman():
    """
    Function to run the game
    """
    # to count user letter entered
    guesses = 0
    # get a word
    selected_word = get_a_word()
    # convert string to list
    word_list = list(selected_word)
    # to print underscores for missing letters
    blank_spaces = "_" * len(selected_word)
    # convert string to list
    blanks_list = list(blank_spaces)
    # copy of the spaces list to check with the original
    new_blanks_list = list(blank_spaces)
    # store letters that user entered
    guess_list = []
    print("Now you can play Hangman!\n")
    # print the gallows
    print_gallows(guesses, selected_word)
    print("\n")
    print(' '.join(blanks_list), end="\n")
    while guesses < 6:
        guess = str(input("Guess a letter: "))
        # always get the letter entered in lower case
        guess = guess.lower()
        # validate user are not entering more than one letter
        if len(guess) > 1:
            print("Stop writing please! Enter one letter at a time.")
        elif guess == "":
            print("Don't you want to play? Enter one letter at a time.")
        elif guess in guess_list:  # check if user is repeating letters
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:  # save the letter entered by the user
            guess_list.append(guess)

            # check and update the list of letters in the selected word
            i = 0
            while i < len(selected_word):
                if guess == selected_word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1
            # if user didnt guess a letter
            if new_blanks_list == blanks_list:
                print("Your letter is wrong.")
                guesses += 1
                # print the gallows
                print_gallows(guesses, selected_word)
                if guesses < 6:
                    print("Guess again.", ' '.join(blanks_list), sep="\n")

            elif word_list != blanks_list:
                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nCONGRATS, YOU WON!!!!:")
                    print("Would you like to play again?")
                    print("Type [y] for yes or [n] for no.")
                    again = str(input("Guess a letter: "))
                    if again == "y":
                        run_hangman()
                    return

                else:
                    print("Right!!!")


if __name__ == '__main__':
    run_hangman()