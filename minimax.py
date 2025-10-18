from game_rules import terminal, moves
from utility import utility
from board import print_board

def minimax(board, player, me='O', opp='X'):
    """Return (best_value, best_move) assuming optimal play by both sides."""
    if terminal(board):
        return utility(board, me, opp), None

    # Initialize best value depending on whose turn it is
    best_val = -2 if player == me else 2
    best_move = None

    for m in moves(board):
        b2 = board[:]
        b2[m] = player
        # Switch turn: if player was me, next is opp; else me
        next_player = opp if player == me else me
        val, _ = minimax(b2, next_player, me, opp)

        if player == me and val > best_val:
            best_val, best_move = val, m
        elif player == opp and val < best_val:
            best_val, best_move = val, m

    return best_val, best_move

if __name__ == "__main__":
    # AI = 'O' to move, human = 'X'
    board = ['X','O','X',
             'O','X',' ',
             ' ','O',' ']
    print_board(board)
    val, move = minimax(board, player='O', me='O', opp='X')
    print("Minimax suggests move:", move, "with value:", val)