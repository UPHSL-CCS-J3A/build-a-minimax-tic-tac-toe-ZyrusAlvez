from game_rules import terminal, moves
from utility import utility

def alphabeta(board, player, alpha=-2, beta=2, me='O', opp='X'):
    if terminal(board):
        return utility(board, me, opp), None
    
    if player == me:
        best = (-2, None)  # MAX
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, opp, alpha, beta, me, opp)
            if val > best[0]:
                best = (val, m)
            alpha = max(alpha, val)
            if alpha >= beta:  # prune
                break
        return best
    else:
        best = (2, None)   # MIN
        for m in moves(board):
            b2 = board[:]; b2[m] = player
            val, _ = alphabeta(b2, me, alpha, beta, me, opp)
            if val < best[0]:
                best = (val, m)
            beta = min(beta, val)
            if alpha >= beta:  # prune
                break
        return best