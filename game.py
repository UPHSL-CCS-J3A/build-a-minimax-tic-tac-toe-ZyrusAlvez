from game_rules import terminal, moves, winner
from utility import utility
from board import print_board
from minimax import minimax

def play_game():
    board = [' '] * 9
    human = 'X'
    ai = 'O'

    print("Welcome to Tic-Tac-Toe (You are X, AI is O)")
    print_board(board)
    first = input("Do you want to go first? (y/n): ").strip().lower().startswith('y')
    current = human if first else ai

    while not terminal(board):
        if current == human:
            # Human move
            try:
                pos = int(input("Enter your move (1-9): ")) - 1
            except ValueError:
                print("Please enter a number 1-9.")
                continue
            if pos not in moves(board):
                print("Invalid move. Try again.")
                continue
            board[pos] = human
        else:
            # AI move
            print("AI is thinking...")
            _, m = minimax(board, player=ai, me=ai, opp=human)
            board[m] = ai
            print(f"AI chose position {m+1}")

        print_board(board)
        current = ai if current == human else human

    w = winner(board)
    if w == human:
        print("🎉 You win!")
    elif w == ai:
        print("🤖 AI wins!")
    else:
        print("😐 It's a draw!")

if __name__ == "__main__":
    play_game()