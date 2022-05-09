import random

count = 3
print("Welcome from our Number Guessing Game ")
while True:
    num = random.randint(0, 10)

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
        elif user_input > 11:
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
                count = 3
    print("The Number is {} ".format(num))
    print(" ")
    again = input("Do you want to play again?(Y/N) : ")
    print(" ")
    while again.lower() != 'y' and again.lower() != 'n':
        print(" ")
        again = input("Invalid Input.Input Y or N only : ")
        print(" ")
        continue

    if again == 'n':
        print("Bye Bye")
        print("--------------------------------")
        break
