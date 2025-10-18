# Tic-Tac-Toe AI with Minimax & Alpha-Beta Pruning

A simple implementation of a Tic-Tac-Toe game where an AI player uses minimax and alpha-beta pruning algorithms to make optimal moves.

## What is Minimax?

Minimax is a decision-making algorithm used in turn-based games. It works by looking at all possible future moves and choosing the best one.

**The basic idea:**

When it's your turn, you want to pick the move that gives you the best outcome. When it's your opponent's turn, they want to pick the move that gives you the worst outcome.

Minimax simulates this back-and-forth:
- The AI explores every possible move
- For each move, it imagines what the opponent would do
- It keeps going until the game ends (win, loss, or draw)
- Then it assigns scores: win = +1, loss = -1, draw = 0
- It picks the move that leads to the best score, assuming the opponent plays perfectly too

**Simple example:**

Imagine you're one move away from winning. Minimax will:
1. See that if you make that move, you win (+1)
2. See that all other moves are worse
3. Choose the winning move

## What is Alpha-Beta Pruning?

Alpha-beta pruning is a smart shortcut that makes minimax faster without changing the result.

**The basic idea:**

While exploring moves, if you find something that's definitely worse than what you already have, you can skip exploring it further.

**Simple example:**

You're looking at two possible moves:
- Move A: You already know it guarantees at least a draw
- Move B: After checking a bit, you realize your opponent can force you to lose if you take it

At this point, you stop exploring Move B completely. Why waste time looking at all the ways you could lose when you already have a better option?

This "pruning" (cutting off branches) saves a lot of time, especially in early game positions where there are many possibilities.

## Alpha-Beta Pruning Performance

**Node counts:**
- Minimax explores every possible game state
- Alpha-beta explores only the necessary ones
- In Tic-Tac-Toe, alpha-beta typically explores 50-70% fewer nodes

**Example comparison:**
- Early game position: Minimax might check 5,000 possibilities
- Same position with alpha-beta: Only checks about 2,000 possibilities
- Both find the exact same best move
- Alpha-beta is just faster

## How the Implementation Works

**Minimax function:**
- Takes the current board and whose turn it is
- Tries every possible move
- For each move, calls itself recursively to see what happens next
- Returns the best move and its value

**Alpha-Beta function:**
- Does everything minimax does
- But also keeps track of alpha (best guaranteed for maximizer) and beta (best guaranteed for minimizer)
- When it finds that a branch can't possibly be better, it stops exploring that branch
- Returns the same result as minimax, just faster

**Main game:**
- Human plays as X, AI plays as O
- AI uses alpha-beta to decide its moves
- Game continues until someone wins or it's a draw
- You can easily switch to minimax by changing line 31 in main.py from `alphabeta(...)` to `minimax(...)`

## Running the Game

Start the game and choose whether to go first. Enter moves using numbers 1-9 for board positions:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

The AI will respond with its optimal move each turn.

## Reflection

Alpha-beta works like minimax — it checks future moves. But if it finds a move that's already worse than another option, it stops looking at the rest. This saves time because those moves won't matter anyway. So, it makes the decision faster without changing the result.

The key insight is that you don't need to explore everything to find the best answer. By keeping track of what you already know, you can safely skip large portions of the search and still guarantee you find the optimal move.