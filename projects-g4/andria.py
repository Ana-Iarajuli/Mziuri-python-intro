import random
def choose_word():
    words = ["apple", "banana", "orang", "grape", "watermelon", "strowberry", "pineapple"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def draw_hangman(attempts):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        '''
    ,
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        '''
    ,
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        '''
    ,
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        '''
    ,
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
        '''
    ,
        '''
           --------
           |      |
           |      O
           |
           |
           |
        '''
    ,
        '''
           --------
           |      |
           |
           |
           |
           |
        '''
    ]
    # davitanje amis daxatvaze
    return stages[attempts]

def hangman():
    word_to_guess = choose_word()
    guessed = []
    attempts = 6

    print("Welcome to hangman!")
    print(display_word(word_to_guess, guessed))

    while True:
        print(draw_hangman(attempts))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")
            if attempts == 0:
                print("Sorry, you're out of attempts! The word was:", word_to_guess)
                break
        else:
            print("sagol")

        word_display = display_word(word_to_guess, guessed)
        print(word_display)

        if all(letter in guessed for letter in word_to_guess):
            print("congratulations, you've guessed the word!")
            break

if __name__ == "__main__":
    # __main__ arvici zustad rasnishnavs
    hangman()

w