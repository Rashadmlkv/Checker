import random

def get_valid_moves(board, a, b):
    valid_moves = []
    piece = board[a][b]
    if piece == 2:  # White piece
        if a > 0:
            if b > 0 and board[a-1][b-1] == 1:
                valid_moves.append((a-1, b-1))
            if b < 7 and board[a-1][b+1] == 1:
                valid_moves.append((a-1, b+1))
        if a > 1:
            if b > 1 and board[a-1][b-1] in [3, 5] and board[a-2][b-2] == 1:
                valid_moves.append((a-2, b-2))
            if b < 6 and board[a-1][b+1] in [3, 5] and board[a-2][b+2] == 1:
                valid_moves.append((a-2, b+2))
    elif piece == 3:  # Black piece
        if a < 7:
            if b > 0 and board[a+1][b-1] == 1:
                valid_moves.append((a+1, b-1))
            if b < 7 and board[a+1][b+1] == 1:
                valid_moves.append((a+1, b+1))
        if a < 6:
            if b > 1 and board[a+1][b-1] in [2, 4] and board[a+2][b-2] == 1:
                valid_moves.append((a+2, b-2))
            if b < 6 and board[a+1][b+1] in [2, 4] and board[a+2][b+2] == 1:
                valid_moves.append((a+2, b+2))
    return valid_moves



def ai_make_move(board):
    valid_pieces = [(i, j) for i in range(8) for j in range(8) if board[i][j] == 3]
    random.shuffle(valid_pieces)
    
    for a, b in valid_pieces:
        valid_moves = get_valid_moves(board, a, b)
        
        attack_moves = [(c, d) for c, d in valid_moves if abs(c - a) == 2]
        
        if attack_moves:
            for c, d in attack_moves:
                mid_x = (a + c) // 2
                mid_y = (b + d) // 2
                board[a][b] = 1
                board[c][d] = 3
                board[mid_x][mid_y] = 1 
                return True
        
        elif valid_moves:
            c, d = random.choice(valid_moves)
            board[a][b] = 1
            board[c][d] = 3
            
            return True
    
    return False
