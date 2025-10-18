from game_rules import winner

def utility(board, me='O', opp='X'):
    """Score terminal states from AI perspective: +1 win, -1 loss, 0 draw."""
    w = winner(board)
    if w == me:
        return 1
    elif w == opp:
        return -1
    else:
        return 0  # draw or non-terminal (we only call this at terminal)