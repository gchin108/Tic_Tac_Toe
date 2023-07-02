from random import randint

r1 = ["1️", "️2️", "️3️"]
r2 = ["4️", "5️", "️6️"]
r3 = ["7️️", "8️️", "9️"]

all_rows = r1 + r2 + r3


def show_rows():
    print(f'{all_rows[0:3]}\n{all_rows[3:6]}\n{all_rows[6:9]}')


def check():
    """iterate from the start of all_rows to the end, in steps of 3, using range(0, len(all_rows), 3). At each step,
    we compare the current element (all_rows[x]), the next one (all_rows[x+1]), and the one after that (all_rows[x+2]).
    If all three are the same (all 'x' or all 'o'), we have a winning condition."""
    for x in range(0, len(all_rows), 3):
        if all_rows[x] == all_rows[x + 1] == all_rows[x + 2] == 'x':
            return 'You Win 😄'
        elif all_rows[x] == all_rows[x + 1] == all_rows[x + 2] == 'o':
            return 'Computer Wins 😱'
    # by columns
    for a in range(0, 3):
        if all_rows[a] == all_rows[a + 3] == all_rows[a + 6] == 'x':
            return 'You Win 😄'
        elif all_rows[a] == all_rows[a + 3] == all_rows[a + 6] == 'o':
            return 'Computer Wins 😱'
    # diagonal
    # note without the parentheses here, it won't work
    if (all_rows[0] == all_rows[4] == all_rows[8] == 'x') or (all_rows[2] == all_rows[4] == all_rows[6] == 'x'):
        return 'You Win 😄'
    elif (all_rows[0] == all_rows[4] == all_rows[8] == 'o') or (all_rows[2] == all_rows[4] == all_rows[6] == 'o'):
        return 'Computer Wins 😱'

    return None  # No winner yet


# for x in range(0,3):
#     all_rows[x+6] = 'x'
# show_rows()

def pc_picks():
    while True:
        index = randint(0, len(all_rows) - 1)
        if all_rows[index] not in ['x', 'o']:
            return index


def start_game():
    turn = 0
    while True:
        turn += 1
        while True:
            user_pick = int(input(f'\nPick a number: ')) - 1
            if all_rows[user_pick] not in ['x', 'o']:
                all_rows[user_pick] = 'x'
                break
            else:
                print("Invalid move, try again.")
        all_rows[pc_picks()] = 'o'
        show_rows()
        check()
        if check() == 'You Win 😄':
            print(check())
            break
        elif check() == 'Computer Wins 😱':
            print(check())
            break
        elif turn == 4:
            print("It's a Draw 😤")
            break


print(f"{r1}\n{r2}\n{r3}")
start_game()
