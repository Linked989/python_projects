board = {'7':'*','8':'*','9':'*',
         '4':'*','5':'*','6':'*',
         '1':'*','2':'*','3':'*',}

def display_board():
    print(board['7'] + "|" + board['8'] + "|" + board['9'])
    print('-+-+-')
    print(board['4'] + "|" + board['5'] + "|" + board['6'])
    print('-+-+-')
    print(board['1'] + "|" + board['2'] + "|" + board['3'])
    print()

def game():
    turn = 'X'
    count = 0

    for i in range(9):
        print(f"Turn: {turn}")
        display_board()

        player = input("Your turn: ")
        if board[player] == '*':
            board[player] = turn
            count += 1

        else:
            print("You can't place x/o there!")
            continue

        #Winning conditions!
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != '*' :
                print(f"Player '{turn}' won!")
                break
            elif board['4'] == board['5'] == board['6'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['1'] == board['2'] == board['3'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['7'] == board['4'] == board['1'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['8'] == board['5'] == board['2'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['9'] == board['6'] == board['3'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['1'] == board['5'] == board['9'] != '*':
                print(f"Player '{turn}' won!")
                break
            elif board['3'] == board['5'] == board['7'] != '*':
                print(f"Player '{turn}' won!")
                break

        #Select players turn
        if turn == 'X':
            turn = '0'
        else:
            turn = 'X'  

        # Keep count of the inputs (prints tie)
        if count == 9:
            print('Tie!')

    #Replay or exit game!
    replay = input("You want to play again (y/n)? ")
    if replay == 'y':
        for key in board:
            board[key] = '*'
        game()

if __name__ == "__main__":
    game()
