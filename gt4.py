import random


def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")


def check_win(board, sign):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == sign:
            return True
    return False


def get_empty_spaces(board):
    return [i for i, x in enumerate(board) if x == " "]


def make_move(board, cell, sign):
    board[cell] = sign


def ai_move(board, sign):
    empty_spaces = get_empty_spaces(board)
    move = random.choice(empty_spaces)
    make_move(board, move, sign)


def game_loop():
    board = [" " for _ in range(9)]
    while True:
        print_board(board)
        move = int(input("Your move: ")) - 1
        if move not in get_empty_spaces(board):
            print("Invalid move. Try again.")
            continue
        make_move(board, move, "X")
        if check_win(board, "X"):
            print_board(board)
            print("You win!")
            break
        if len(get_empty_spaces(board)) == 0:
            print_board(board)
            print("It's a draw.")
            break
        print("AI's turn.")
        ai_move(board, "O")
        if check_win(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        if len(get_empty_spaces(board)) == 0:
            print_board(board)
            print("It's a draw.")
            break


print_board(board=['' for _ in range(9)])
