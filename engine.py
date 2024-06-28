import main

def moves(board, row, col):
    down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
    length = board.get_length()
    piece = board.get(row, col)

    bottom = []
    top = []

    if piece:
        for (x, y) in down:
            if (0 <= (row + x) < length) and (0 <= (col + y) < length) and board[row + x][col + y] == 1:
                bottom.append((row + x, col + y))

        for (x, y) in up:
            if (0 <= (row + x) < length) and (0 <= (col + y) < length) and board[row + x][col + y] == 1:
                top.append((row + x, col + y))
            
        if piece == 4 or piece == 5:
            return sorted(bottom + top)
        
        if piece.is_black():
            return sorted(bottom)
        


    return []