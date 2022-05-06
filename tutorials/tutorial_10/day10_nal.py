def board(values):
    print("\n")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('_____|_____|_____')

    print("     |     |")
    print("  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('_____|_____|_____')

    print("     |     |")

    print("  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("     |     |")
    print("\n")


def print_scoreboard(score_board):
    print("--------------------------------")
    print("        SCOREBOARD       ")
    print("--------------------------------")

    players = list(score_board.keys())
    print(players[0], "\t    ", score_board[players[0]])
    print(players[1], "\t    ", score_board[players[1]])

    print("--------------------------------")
    print(" ")


def check_win(p_pos, current_player):

    list = [[1, 2, 3], [3, 6, 9], [4, 5, 6], [1, 5, 9], [1, 4, 7],
            [2, 5, 8], [7, 8, 9], [3, 5, 7]]

    for i in list:
        if all(j in p_pos[current_player] for j in i):

            return True

    return False


def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def single_game(current_player):

    values = [' ' for i in range(9)]

    player_pos = {'X': [], 'O': []}

    while True:
        board(values)

        try:
            print("Player ", current_player, " turn. Which box? : ")
            play = int(input())
        except ValueError:
            print("Wrong Input!!! Try Again")
            continue

        if play < 1 or play > 9:
            print("Wrong Input!!! Try Again")
            continue

        if values[play-1] != ' ':
            print("Place already filled. Try again!!")
            continue

        values[play-1] = current_player

        player_pos[current_player].append(play)

        if check_win(player_pos, current_player):
            board(values)
            print("Player ", current_player, " has won the game!!")

            print("\n")
            return current_player

        if check_draw(player_pos):
            board(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


print("Player 1")
p1 = input("Enter the name : ")
print(" ")

print("Player 2")
p2 = input("Enter the name : ")
print(" ")

current_player = p1

player_choice = {'X': "", 'O': ""}

options = ['X', 'O']

score_board = {p1: 0, p2: 0}
print_scoreboard(score_board)

while True:

    print("Turn to choose for", current_player)
    print("Enter 1 for X")
    print("Enter 2 for O")
    print("Enter 3 to Quit")

    try:
        choice = int(input())
    except ValueError:
        print("Wrong Input!!! Try Again\n")
        continue

    if choice == 1:
        player_choice['X'] = current_player
        if current_player == p1:
            player_choice['O'] = p2
        else:
            player_choice['O'] = p1

    elif choice == 2:
        player_choice['O'] = current_player
        if current_player == p1:
            player_choice['X'] = p2
        else:
            player_choice['X'] = p2

    elif choice == 3:
        print_scoreboard(score_board)
        break

    else:
        print("Wrong Choice!!!! Try Again\n")

    winner = single_game(options[choice-1])

    if winner != 'D':
        player_won = player_choice[winner]
        score_board[player_won] = score_board[player_won] + 1

    print_scoreboard(score_board)

    if current_player == p1:
        current_player = p2
    else:
        current_player = p1
