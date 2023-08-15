"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                xcount += 1
            if board[row][col] == O:
                ocount += 1
    if xcount > ocount:
        return O
    elif ocount > xcount:
        return X
    else:
        return None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleactions = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                possibleactions.append(row,col)
    return possibleactions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newboard = deepcopy(board)
    if newboard[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Move")
    else:
        newboard[action[0]][action[1]] = player(newboard)
        return newboard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0

def minvalue(board):
    if terminal(board):
        return utility(board)
    value = math.inf
    for action in actions(board):
        value = min(value, maxvalue(result(board, action)))
    return value
def maxvalue(board):
    if terminal(board):
        return utility(board)
    value = -math.inf
    for action in actions(board):
        value = max(value, minvalue(result(board, action)))
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    currentplayer = player(board)
    if currentplayer == X:
        value = -math.inf
        for action in actions(board):
            newvalue = minvalue(result(board, action))
            if newvalue > value:
                value = newvalue
                bestaction = action
    elif currentplayer == O:
        value = math.inf
        for action in actions(board):
            newvalue = maxvalue(result(board, action))
            if newvalue < value:
                value = newvalue
                bestaction = action
    return bestaction
