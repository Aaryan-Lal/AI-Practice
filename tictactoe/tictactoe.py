"""
Tic Tac Toe Player
"""

import math
import copy

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
    X_count = 0
    O_count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == X:
                X_count = X_count + 1
            elif board[i][j] == O:
                O_count = O_count + 1

    if X_count == O_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    if action not in actions(board):
        raise Exception("This is not a valid move, choose another move")

    new_board = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2]:
            if board[i][0] == X or board[i][0] == O:
                return board[i][0]
        if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
            if board[0][i] == X or board[0][i] == O:
                return board[0][i]

    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == X or board[0][0] == O:
            return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == X or board[0][2] == O:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if winner(board) is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value((result(board, action))))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value((result(board, action))))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    if player(board) == X:
        v = -math.inf
        chosen_action = None
        for action in actions(board):
            minimised_option = min_value(result(board, action))
            if minimised_option > v:
                v = minimised_option
                chosen_action = action
    elif player(board) == O:
        v = math.inf
        chosen_action = None
        for action in actions(board):
            maximised_option = max_value(result(board, action))
            if maximised_option < v:
                v = maximised_option
                chosen_action = action
    return chosen_action
