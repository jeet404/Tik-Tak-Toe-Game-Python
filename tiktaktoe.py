board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

game_going = True

winner = None

current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    # initial board
    display_board()

    while game_going:

        #single turn 
        handle_turn(current_player)

        #check if game has ended
        check_if_game_over()

        #flip to other player
        flip_player()

    # game ended
    if winner == "X" or winner == "O":
        print(winner + "Won.")
    elif winner == None:
        print("Tie.")

#handle single turn of player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose Position 1 to 9 : ")

    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("Choose Position 1 to 9 : ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there . Go Again.")

    board[position] = player 
    display_board()

def check_if_game_over():
    check_for_winnner()
    check_for_tie()

def check_for_winnner():
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    global game_going

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return

def check_columns():
    global game_going

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_going = False
        
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    return

def check_diagonals():
    global game_going

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[6] == board[4] == board[2] != "-"

    if diagonal1 or diagonal2:
        game_going = False
        
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[6]
    return

def check_for_tie():
    global game_going
 
    if "-" not in board:
        game_going = False
        return True
    else:
        return False
    return

def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player= "X"
    return

play_game()