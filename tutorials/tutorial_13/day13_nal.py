import random

print("Welcome from our Number Guessing Game")


def guessing_game():
    count = 3
    num = random.randint(0, 10)
    print(num)

    while True:

        try:
            user_input = int(input("Enter Number : "))
            print(" ")
        except ValueError:
            print("Invaild Input.Input Valid Number Again.")
            print(" ")
            continue

        else:
            if user_input == num:
                print("U Won")
            elif user_input < 0:
                print(" ")
                print("Invalid Input.Input Can`t be Negative. ")
                print(" ")
                continue
            elif user_input > 10:
                print(" ")
                print("Invalid Input.Guess number between 0 to 10")
                print(" ")
                continue
            else:
                if count != 1:
                    count -= 1
                    print(" ")
                    print("Try Again.You have {} time left to guess.".format(count))
                    continue
                else:
                    print("You lost.You have no time left to guess number.")

        again()


def again():
    user_again = str(input("Let's play next game?? (Y/N)"))
    print(" ")
    if user_again.lower() == "y":
        guessing_game()
    elif user_again.lower() == "n":
        print("Bye Bye")
    else:
        print("Please enter Y or N only ")
        again()


guessing_game()
