import random


def game():
    info = input(
        "Welcome to Rock,Paper,Scissors!Press Enter to start game. ")

    if info in '\n':

        user_score = 0
        computer_score = 0

        while True:
            user_input = str(
                input("Let`s start! Rock Paper or Scissors?: "))
            computer = ' '
            if user_input.lower() != 'rock' and user_input.lower() != 'paper' and user_input.lower() != 'scissors':
                print("Wrong Choice!Choice Again...")
                continue
            else:
                random_computer = random.randint(0, 2)
                if random_computer == 0:
                    computer = 'rock'
                elif random_computer == 1:
                    computer = 'paper'
                elif random_computer == 2:
                    computer = 'scissors'
                print(" ")
                print("Your choice : ", user_input.lower())
                print("Computer choice : ", computer)

                if user_input == 'rock':
                    if computer == 'rock':
                        print("Draw")
                    elif computer == 'scissors':
                        print("You Win!")
                        user_score += 1
                    elif computer == 'paper':
                        print("You Lose!")
                        computer_score += 1

                elif user_input == 'paper':
                    if computer == 'paper':
                        print("Draw")
                    elif computer == 'rock':
                        print("You Win!")
                        user_score += 1
                    elif computer == 'scissors':
                        print("You Lose!")
                        computer_score += 1

                elif user_input == 'scissors':
                    if computer == 'scissors':
                        print("Draw")
                    elif computer == 'paper':
                        print("You Win!")
                        user_score += 1
                    elif computer == 'rock':
                        print("You Lose!")
                        computer_score += 1
                print("-------------------------------------")
                print("You have ", user_score, " wins")
                print("The computer has ", computer_score, " wins")

                again()
                break

    else:
        print("Press Enter Only Please ")
        game()


def again():

    restart = input("Play Again!(Y,N) ")

    if restart.lower() == "y":
        game()
    elif restart.lower() == "n":
        print("Bye Bye")
        print("---------------------------------------")

    else:
        print("Choose only Y or N")
        print("---------------------------------------")
        again()


game()
