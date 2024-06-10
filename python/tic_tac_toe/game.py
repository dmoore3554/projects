"""
A 2 player game of tic tac toe built in Python.
"""

def print_game_board(game_board):
    """
    Formats and prints the game board to console.
    """
    print("    1   2   3  ")
    for i in range(len(game_board)):
        print(f"{i + 1} ", end="")
        for item in game_board[i]:
            print(f"| {item} ", end="")
        print("|")
    print()

def take_turn():
    """
    Prompts the player to choose a place to play.
    """
    good_input = False
    while not good_input:
        try:
            good_input = True
            row = int(input("Choose a row to play in: "))
            column = int(input("Choose a column to play in: "))
            if row < 1 or row > 3 or column < 1 or column > 3:
                print(row,column)
                print("Invalid input. Try again.")
                good_input = False
        except:
            print("Invalid input. Try again.")
            good_input = False
    print()
    return (row - 1, column - 1)

def determine_winner(game_board):
    """
    Determines if there is a winner to the game and returns who won.
    """
    for i in range(len(game_board)):
        # Horizontal Rows
        if all(j == game_board[i][0] and j != " " for j in game_board[i]):
            return game_board[i][0]
        # Vertical Columns
        if all(game_board[0][i] == game_board[k][i] and game_board[0][i] != " " for k in range(3)):
            return game_board[0][i]
    # Diagonals
    if all(game_board[0][0] == game_board[i][i] and game_board[0][0] != " " for i in range(3)):
        return game_board[0][0]
    if all(game_board[2][0] == game_board[2 - i][i] and game_board[2][2] != " " for i in range(3)):
        return game_board[2][0]
    return False
        

def game():
    """
    The main game loop.
    """
    game_board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    turn_count = 1
    game_over = False
    while not game_over:
        if turn_count >= 10:
            print("It's a tie!")
            print_game_board(game_board)
            break
        
        print_game_board(game_board)
        
        if turn_count % 2 == 1:
            print("It's Player 1's Turn!")
            marker = "X"
        else:
            print("It's Player 2's Turn!")
            marker = "O"
        row, column = take_turn()
        while game_board[row][column] is not " ":
            print("A player has already gone there! Try again.")
            row, column = take_turn()
        game_board[row][column] = marker
        turn_count += 1
        
        winner = determine_winner(game_board)
        if winner:
            if winner == "X":
                print("Player 1 wins!")
            elif winner == "O":
                print("Player 2 wins!")
            print_game_board(game_board)
            game_over = True

if __name__ == "__main__":
    game()
