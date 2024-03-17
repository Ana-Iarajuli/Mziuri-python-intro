import random
word_list = ["xawapuri", "burgir", "cxeli", "dzagli", "jasu", "bek"]   #აქ მას ნებისმიერი სიტყვა შეიყვანეთ

def play_word_jumble():
    while True:
        random_word = random.choice(word_list)
        random_word1 = list(random_word)
        random.shuffle(random_word1)
        x = "".join(random_word1)

        print("Jumbled Word:", x)
        user_guess = input("Your Guess: ")

        if user_guess == 'quit':
            break

        if user_guess == random_word:
            print("correct!")

        else:
            print("Incorrect. correct word was:", random_word)


play_word_jumble()