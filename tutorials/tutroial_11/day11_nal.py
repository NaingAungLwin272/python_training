import random
user_score = 0
computer_score = 0
computer = ' '
input("Welcome to Rock,Paper,Scissors!Press Enter to start game. ")


while True:

    user_input = str(
        input("Let`s start! Rock Paper or Scissors?: "))

    while user_input.lower() != 'rock' and user_input.lower() != 'paper' and user_input.lower() != 'scissors':
        user_input = input("Invalid Input.Input A Valid One Please : ")

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

    restart = input("Play Again!(Y,N) ")

    while restart.lower() != "y" and restart.lower() != "n":
        restart = input("Invalid Input.Input Y or N only :  ")
    if restart.lower() == 'n':
        print("Bye Bye!! See you next time")
        break
