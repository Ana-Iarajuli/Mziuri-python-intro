import random

def choose_word():
    word_list = ["shaurma", "hangman", "burgeri", "pizza", "avatari", "mziuri", "snickers"]

    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while True:
        current_display = display_word(word_to_guess, guessed_letters)
        print("Current word: ", current_display)

        guess = input("Guess a letter: ").lower()

        if guess in word_to_guess:
            print("Good guess!")

            guessed_letters.append(guess)
        else:
            print("Wrong guess!")
            attempts_left -= 1

        if set(word_to_guess) == set(guessed_letters):
            print("Sagool: ", word_to_guess)
            break
        elif attempts_left == 0:
            print("Damarcxdi, sityva iyo: ", word_to_guess)
            break

        print("Attempts left: ", attempts_left)

if __name__ == "__main__":
    hangman()