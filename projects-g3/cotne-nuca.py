from random import randint

player_score = 0
computer_score = 0

#qulebis dafis funqcia
def score_board(player_dice_value, computer_dice_value):
    global player_score
    global computer_score

    player_score += player_dice_value
    computer_score += computer_dice_value

    print()
    print("#" * 20)
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("#" * 20)
    print()


#shesavali
welcome_message = """
          Welcome to 'Pig', a dice game!

    In this game, a user and a computer opponent
    roll a 6-sided die each round. If the value of
    the die is a 1, the player that rolled the 1 loses
    all of their points. Otherwise, the player gets the
    value of the die added to their points. The first
    player to reach 30 points wins!
"""
print(welcome_message)


#tamashis dawyeba
player_name = input("what's your name?")
start_game = input(f"Press 'Enter' to roll the die {player_name}!\n")



while True:
    #kamatlis gagoreba
    player_dice_value = randint(1, 6)
    computer_dice_value = randint(1, 6)

    print(f"{player_name} rolls a {player_dice_value}")
    print(f"computer rolls a {computer_dice_value}")

    # tu 1 gagorda qulebi gakldeba
    if player_dice_value == 1:
        print()
        print("all of your points have been deducted")
        player_score = 0 #unda iyos player_dice_value
        player_dice_value = 0

    if computer_dice_value == 1:
        print()
        print("all of computers points have been deducted")
        computer_score = 0 # unda iyos computer_dice_value
        computer_dice_value = 0

    #score board funqcia
    score_board(player_dice_value, computer_dice_value)

    #wageba mogeba da tamashis shewyveta
    if player_score >= 30:
        print(f"{player_name} wins!")
        break

    elif computer_score >= 30:
        print("Computer wins!")
        break

    continue_game = input(f"Press 'Enter' to roll again!\n")