import random

def start_the_game():
    while True:

        x=input("hello do you want to play the game (yes or no):")

        if x.lower() != "yes":
            exit()
        y = random.randint(1, 10)
        while x.lower() == "yes":


            try:
                z=int(input("guess the number from 1 to 10:"))
                if z < 1 or z >10:
                    print("that's not possible")
                else:

                    if z==y:
                        print("wow wow congratulations")


                        d = input("do you want to continue the game (yes or no):")
                        if d.lower() != "yes":
                            break
                        elif d.lower() =="yes":
                            y = random.randint(1, 10)
                            continue

                    elif z< y:
                        print("no no the number is bigger:")
                    elif z>y:
                        print("no no the number is lower:")
            except ValueError:
                print("you entered invalid number")


print(start_the_game())

