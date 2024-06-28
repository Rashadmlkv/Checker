import main as mn
import copy

def heuristics(state):
    """
    This is the heuristics function. This function calculates these metrics:
        a. Normalized utility values from the number of pawn and king pieces 
            on the board. [0.32, -0.32]
        b. Normalized utility values from the number of captures could be made 
            by kings and pawns. [0.96, -0.96]
        c. Normalized utility values from the distances of pawns to become
            kings. [0.70, -0.70]
        d. Normalized utility values from the number of pieces on the safer
            places on the board. [0.19, -0.19]
    """
    board = state[0]
    turn = state[1]
    length = board.get_length()
    bp, wp = 0, 0
    bk, wk = 0, 0
    bc, wc = 0, 0
    bkd, wkd = 0, 0
    bsd, wsd = 0.0, 0.0
    for row in range(length):
        for col in range(length):
            piece = board.get(row, col)
            if piece:
                r = row if row > (length - (row + 1)) else (length - (row + 1))
                c = col if col > (length - (col + 1)) else (length - (col + 1))
                d = int(((r ** 2.0 + c ** 2.0) ** 0.5) / 2.0)
                if piece.color() == 'black':
                    bc += sum([len(v) for v in mn.get_captures(board, row, col)])
                    if piece.is_king():
                        bk += 1
                    else:
                        bp += 1
                        bkd += row + 1
                        bsd += d
                else:
                    wc += sum([len(v) for v in mn.get_captures(board, row, col)])
                    if piece.is_king():
                        wk += 1
                    else:
                        wp += 1
                        wkd += length - (row + 1)
                        wsd += d
    if turn == 'black':
        black_count_heuristics = \
                3.125 * (((bp + bk * 2.0) - (wp + wk * 2.0)) \
                    / 1.0 + ((bp + bk * 2.0) + (wp + wk * 2.0)))
        
        black_capture_heuristics = 1.0417 * ((bc - wc)/(1.0 + bc + wc))
        
        black_kingdist_heuristics = 1.429 * ((bkd - wkd)/(1.0 + bkd + wkd))
        
        black_safe_heuristics = 5.263 * ((bsd - wsd)/(1.0 + bsd + wsd))
        
        return black_count_heuristics + black_capture_heuristics \
                    + black_kingdist_heuristics + black_safe_heuristics
    else:
        white_count_heuristics = \
                3.125 * (((wp + wk * 2.0) - (bp + bk * 2.0)) \
                    / 1.0 + ((bp + bk * 2.0) + (wp + wk * 2.0)))
        
        white_capture_heuristics = 1.0416 * ((wc - bc)/(1.0 + bc + wc))
        
        white_kingdist_heuristics = 1.428 * ((wkd - bkd)/(1.0 + bkd + wkd))
        
        white_safe_heuristics = 5.263 * ((wsd - bsd)/(1.0 + bsd + wsd))
        
        return white_count_heuristics + white_capture_heuristics \
                    + white_kingdist_heuristics + white_safe_heuristics
                    
def is_terminal(state, maxdepth = None):
    """
    Determines if a tree node is a terminal or not.
    Returns boolean True/False.
    """
    board = state[0]
    turn = state[1]
    depth = state[2]
    (moves, captures) = mn.get_hints(board, turn)
    if maxdepth is not None:
        return ((not moves) and (not captures)) or depth >= maxdepth
    return ((not moves) and (not captures))

def transition(state, action, ttype):
    """
    This is the transition function. Given a board state and action,
    it transitions to the next board state.
    """
    board = copy.deepcopy(state[0])
    turn = state[1]
    depth = state[2]
    if ttype == "move":
        mn.apply_move(board, action)
    elif ttype == "jump":
        mn.apply_capture(board, action)
    turn = 'white' if state[1] == 'black' else 'black'
    depth += 1
    return (board, turn, depth)

def maxvalue(state, maxdepth, alpha = None, beta = None):
    """
    The maxvalue function for the adversarial tree search.
    """
    board = state[0]
    turn = state[1]
    if is_terminal(state, maxdepth):
        return heuristics(state)
    else:
        v = float('-inf')
        (moves, captures) = mn.get_hints(board, turn)
        if captures:
            for a in captures:
                v = max(v, minvalue(transition(state, a, "jump"), \
                        maxdepth, alpha, beta))
                if alpha is not None and beta is not None:
                    if v >= beta:
                        return v
                    alpha = max(alpha, v)
            return v
        elif moves:
            for a in moves:
                v = max(v, minvalue(transition(state, a, "move"), \
                        maxdepth, alpha, beta))
                if alpha is not None and beta is not None:
                    if v >= beta:
                        return v
                    alpha = max(alpha, v)
            return v            

def minvalue(state, maxdepth, alpha = None, beta = None):
    board = state[0]
    turn = state[1]
    if is_terminal(state, maxdepth):
        return heuristics(state)
    else:
        v = float('inf')
        (moves, captures) = mn.get_hints(board, turn)
        if captures:
            for a in captures:
                v = min(v, maxvalue(transition(state, a, "jump"), \
                                     maxdepth, alpha, beta))
                if alpha is not None and beta is not None:
                    if v <= alpha:
                        return v
                    beta = min(beta, v)
            return v
        elif moves:
            for a in moves:
                v = min(v, maxvalue(transition(state, a, "move"), \
                                     maxdepth, alpha, beta))
                if alpha is not None and beta is not None:
                    if v <= alpha:
                        return v
                    beta = min(beta, v)
            return v

def minimax_search(state, maxdepth = None):
    """
    The depth limited minimax tree search.
    """
    board = state[0]
    turn = state[1]
    (moves, captures) = mn.get_hints(board, turn)
    if captures:
        return max([(a, minvalue(transition(state, a, "jump"), maxdepth)) \
                        for a in captures], key = lambda v: v[1])
    elif moves:
        return max([(a, minvalue(transition(state, a, "move"), maxdepth)) \
                        for a in moves], key = lambda v: v[1])        
    else: 
        return ("pass", -1)

def get_next_move(board, turn):
    state = (board, turn, 0)
    move = minimax_search(state, 7)
    return move[0]