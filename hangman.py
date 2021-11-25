# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if not (char in letters_guessed):
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    remin = ''
    for char in secret_word:
        remin += (char if char in letters_guessed else '_ ')
    return remin



def get_available_letters(letters_guessed):
    all_letters = string.ascii_lowercase
    available_letters = ''
    for char in all_letters:
        if not (char in letters_guessed):
            available_letters += char
    return available_letters



def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long")
    print("-------------")
    turns = 6
    mistakesMade = ''
    lettersGuessed = []
    "\n"
    wordIsGuessed = False
    avl = list(get_available_letters(lettersGuessed))
    gamedone1 = False
    gamedone2 = False

    while True:
        get_guessed_word(secret_word, lettersGuessed)
        print('You have ' + str(turns) + ' guesses left')
        print('Available letters: ' + str(get_available_letters(lettersGuessed)))
        guess = input('Type guess a letter: ')
        guess = guess.lower()
        #print(secret_word)
        if guess in get_available_letters(lettersGuessed):
            turns = turns - 1
        else:
            turns = turns
        lettersGuessed = lettersGuessed + list(guess)
        if guess in secret_word:
            print('Good guess: ' + str(get_guessed_word(secret_word, lettersGuessed)))
            print("-------------")
            if is_word_guessed(secret_word, lettersGuessed) == True:
                gamedone1 = True
        elif guess not in secret_word and turns != 0:
            print('Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, lettersGuessed)))
            print('-------------')

        if turns == 0:
            gamedone2 = True
        if gamedone1:
            print('Congratulations, you won!')
            break
        if gamedone2:
            print("Sorry, you ran out of guesses. The word was " + str(secret_word))
            break






def match_with_gaps(my_word, other_word):
    len_my_word = len(my_word.replace(" ", ""))

    len_other_word = len(other_word)


    other_list = list(other_word)
    my_list = list(my_word.replace(" ", "").replace("_", ""))  # スペースと"_"を除いたmy_wordのリスト

    if bool(my_list):
        if len_my_word == len_other_word:
            for w in my_list:
                if my_list.count(w) == other_list.count(w):
                    if w in other_list:

                        if [k for k, x in enumerate(list(my_word.replace(" ", ""))) if x == w] == \
                                [k for k, x in enumerate(other_list) if x == w]:
                            accuracy = True
                            continue
                        else:
                            accuracy = False
                            break
                    else:
                        accuracy = False
                        break
                else:
                    accuracy = False
                    break

        else:
            accuracy = False
    else:
        if len_my_word == len_other_word:
            accuracy = True

    return accuracy



def show_possible_matches(my_word):
    hint_list = []

    for word in wordlist:
        # print(word)
        if match_with_gaps(my_word, word) == True:
            hint_list.append(word)

    return hint_list



def hangman_with_hints(secret_word):
    print('Welcome to the game Hangman!')
    length_of_letter = len(secret_word)

    print('I am thinking of a word that is', length_of_letter, 'letters long.')

    left_num_guesses = 6
    left_num_worning = 3
    letters_guessed = []
    vowel = ['a', 'i', 'u', 'e', 'o']
    num_of_try = 0
    num_of_secretword = len(secret_word)

    print('----------')

    while left_num_guesses > 0:
        print('You have', left_num_guesses, 'guesses left.')
        print('Available letters:', ''.join(get_available_letters(letters_guessed)))

        input_letter_all = str(input('Please guess a letter:'))
        input_letter = input_letter_all.lower()

        available_list = get_available_letters(letters_guessed)

        if input_letter == '*':
            if length_of_letter - get_guessed_word(secret_word, letters_guessed).count("_") == 0:
                print("You should guess at least one letter!")
                continue
            else:
                print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))

        elif input_letter in available_list:
            if input_letter in list(secret_word):
                letters_guessed.append(input_letter)
                print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
            else:
                letters_guessed.append(input_letter)
                print('Oops! That letter is not in my word: ', \
                      get_guessed_word(secret_word, letters_guessed))
                if input_letter in vowel:
                    left_num_guesses -= 2
                else:
                    left_num_guesses -= 1

        elif input_letter in letters_guessed:
            letters_guessed.append(input_letter)
            if left_num_worning > 0:
                left_num_worning -= 1
                print("Oops! You've already guessed that letter. You now have", left_num_worning, \
                      "warnings:", get_guessed_word(secret_word, letters_guessed))
            else:
                left_num_guesses -= 1
                print("Oops! You've already guessed that letter. You now have", left_num_guesses, \
                      "gueses:", get_guessed_word(secret_word, letters_guessed))

        else:
            letters_guessed.append(input_letter)
            if left_num_worning > 0:
                left_num_worning -= 1
                print('Oops! That is not a valid letter. You have', left_num_worning, \
                      'warnings left: ', get_guessed_word(secret_word, letters_guessed))
            else:
                left_num_guesses -= 1
                print('Oops! That is not a valid letter. You have', left_num_guesses, \
                      'guesses left: ', get_guessed_word(secret_word, letters_guessed))

        num_of_try += 1

        comparison = len((get_guessed_word(secret_word, letters_guessed))) - \
                     (get_guessed_word(secret_word, letters_guessed)).count("_") - \
                     (get_guessed_word(secret_word, letters_guessed)).count(" ")

        if comparison == num_of_secretword:
            print('Congratulations, you are a winner! ')
            print('Your total score for this game is: ', num_of_try)
            break

        print('----------')

    if left_num_guesses == 0:
        print("YOU are a loser!")

    return

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    hangman(secret_word)


