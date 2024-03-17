import random

def play_word_jumble():
    print('write "quit" if you want to exit the game')
    words = ['jasurbeki', 'jgufi4', 'kargiCxeni']
    random_word = random.choice(words)
    random_word_list = list(random_word)
    random.shuffle(random_word_list)
    jumbled = ''.join(random_word_list)
    print(f'jumbled word is: {jumbled}')

    continue_game = True
    while continue_game:
        guess = input('Enter your guess: ')
        if guess == random_word:
            return 'You Won!'
        else:
            print('incorrect guess')

            try_again = input('do you want to try again?')
            if try_again == 'quit':
                continue_game = False
                return "Thanks for playing"

print(play_word_jumble())