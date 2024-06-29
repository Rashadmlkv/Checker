#!/usr/bin/python3

import board as brd
import input as io
import draw as drw
import aitool as ai
import pygame
import copy


running = True
turn = 3
screen = drw.createWindow()



def indexify(position):
    return (ord(position[0])-ord('a'),int(position[1:])-1)

def deindexify(row, col):
    return chr(row+97)+str(col+1)


def get_jumps(board, row, col, is_sorted = False):
    """
    This function is very similar to the get_moves() function. This function
    lists all the capture for a single piece on the board located at the row,
    col position. To capture the piece needs to "jump". A checker may move 
    more than one space if they can jump one of the opponent's checker pieces 
    which is located immediately in their diagonal vicinity and onto a free 
    space. This function returns a list of valid captures in terms of string 
    positions, like 'a1', 'b4' etc. The rules are follows:
        a. All the captures(s) must be inside the board.
        b. If the given row, col position has no piece (i.e. empty), this
            function returns an empty list.
        c. To make a jump, there must be an opponent piece on the immediate
            diagonal.
        d. If the piece is not a king then it will return a list of at most 
            two diagonal positions. For a black piece, the diagonals will be 
            bottom-left and bottom-right.
        e. If the piece is a king, then it will return a list of at most 
            four diagonal positions. Irrespective of color, the diagonals 
            will be bottom and top, left and right.
        f. By default, is_sorted flag is set to False, if it's True then
            the final returning list must be sorted. Remember that the list
            is a list of string positions.
    """
    down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
    length = 8
    piece = board[row][col]
    if piece:
        bottom = \
            [deindexify(row + 2 * x, col + 2 * y) for (x, y) in down \
             if (0 <= (row + 2 * x) < length) \
                 and (0 <= (col + 2 * y) < length) \
                 and board[row + 2 * x][col + 2 * y] == 1 \
                 and (not board[row + x][col + y] == 1) \
                 and (board[row + x][col + y] != piece)]
        top = \
            [deindexify(row + 2 * x, col + 2 * y) for (x, y) in up \
             if (0 <= (row + 2 * x) < length) \
                 and (0 <= (col + 2 * y) < length) \
                 and board[row + 2 * x][col + 2 * y] == 1 \
                 and (not board[row + x][col + y] == 1) \
                 and (board[row + x][col + y] != piece)]
        
        return (sorted(bottom + top) if (piece == 4 or piece == 5) else \
                (sorted(top) if (piece == 3 or piece == 5) else sorted(bottom))) \
                    if is_sorted else (bottom + top if (piece == 4 or piece == 5) else \
                                       (top if (piece == 3 or piece == 5) else bottom))
    return []


def search_path(board, row, col, path, paths, is_sorted = False):
    """
    This function recursive builds all capturing paths started at a certain
    row/col position. 
    """
    path.append(deindexify(row, col))
    jumps = get_jumps(board, row, col, is_sorted)
    if not jumps:
        paths.append(path)
    else:
        for position in jumps:
            (row_to, col_to) = indexify(position)
            
            piece = copy.copy(board[row][col])
            board[row][col] = 1
            board[row_to][col_to] = piece

            if (piece == 3 and row_to == 7) \
                or (piece == 2 and row_to == 0) \
                and (not (piece == 4 or piece == 5)):
                piece = 4 if piece == 2 else 5
            
            row_mid = row + 1 if row_to > row else row - 1
            col_mid = col + 1 if col_to > col else col - 1
            capture = board[row_mid][col_mid]
            board[row_mid][col_mid] = 1
            
            search_path(board, row_to, col_to, copy.copy(path), paths)
            
            board[row_mid][col_mid] = capture
            board[row_to][col_to] = 1
            board[row][col] = piece


def get_captures(board, row, col, is_sorted = False):
    """
    This function finds all capturing paths started at a certain row/col
    position on the board. If there is no capture from the given row/col,
    this function will return an empty list [].
    """
    paths = []
    board_ = copy.copy(board)
    search_path(board_, row, col, [], paths, is_sorted)
    if len(paths) == 1 and len(paths[0]) == 1:
        paths = []
    return paths


def get_all_moves(board, color, is_sorted = False):
    """
Get all the positions of all the pieces on the board that can be moved.
    use three for loop and three if
return list of all move
    """
    row = col = 8
    final_list = []
    for r in range(row):
        for c in range(col):
            piece = board[r][c]
            if piece:
                if piece == color:
                    path_list = get_moves(board, r, c, is_sorted)
                    path_start = deindexify(r, c)
                    for path in path_list:
                        final_list.append((path_start, path))
    
    if is_sorted == True:
        final_list.sort()
    return final_list


def sort_captures(all_captures,is_sorted=False):
    if is_sorted:
        return sorted(all_captures, key = lambda x: (-len(x), x[0]))
    return all_captures


def get_all_captures(board, color, is_sorted = False):
    row = col = 8
    final_list = []
    for r in range(row):
        for c in range(col):
            piece = board[r][c]
            if piece:
                if piece == color:
                    path_list = get_captures(board, r, c, is_sorted)
                    for path in path_list:
                        final_list.append(path) 
    return sort_captures(final_list, is_sorted)


def get_hints(board, color, is_sorted = False):
    jump = get_all_captures(board, color, is_sorted)
    
    if jump:
        return ([], jump)
    
    move = get_all_moves(board, color, is_sorted)
    return (move, jump)


def apply_capture(board, capture_path):
    """
Performs actual operations and jumps to move the specified pieces.
    use one while loop and one if
No return
    
    Raise this exception below:
        raise RuntimeError("Invalid jump/capture, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no jump found from any position in capture_path, i.e. use 
            tools.get_jumps() function to get all the jumps from a certain
            position in capture_path
        b. the destination position from a jump is not in the jumps list found
            from tools.get_jumps() function.            
    """
    counter = 0
    while counter < len(capture_path)-1:
        path = [capture_path[counter], capture_path[counter + 1]]
        counter += 1
        row,col = indexify(path[0])
        row_end,col_end = indexify(path[1])
        path_list = get_jumps(board, row, col, is_sorted = False)
        
        if path[1] in path_list:
            piece = board[row][col]
            if piece == 2 and row_end == 7 \
            or piece == 3 and row_end == 0:
                piece = 5 if piece == 3 else 4
            
            board[row][col] = 1
            row_eat, col_eat = max(row, row_end)-1, max(col, col_end)-1
            board[row_eat][col_eat] = 1
            board[row_end][col_end] = piece
        else:
            raise RuntimeError("Invalid jump/capture, please type" \
                             + " \'hints\' to get suggestions.")


def get_moves(board, row, col, is_sorted = False):
    """
    This function returns moves for a given single piece at row,col position.
    This function returns a list of valid moves in terms of string positions,
    like 'a1', 'b4' etc. The rules are follows:
        a. All the move(s) must be inside the board.
        b. If the given row, col position has no piece (i.e. empty), this
            function returns an empty list.
        c. If the piece is not a king then it will return a list of at most 
            two diagonal positions. For a black piece, the diagonals will be 
            bottom-left and bottom-right. For a white, they will be top-left 
            and top-right.
        d. If the piece is a king, then it will return a list of at most 
            four diagonal positions. Irrespective of color, the diagonals 
            will be bottom and top, left and right.
        e. By default, is_sorted flag is set to False, if it's True then
            the final returning list must be sorted. Remember that the list
            is a list of string positions.
    """
    down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
    length = 8
    piece = board[row][col]
    if piece:
        bottom = [deindexify(row + x, col + y) for (x, y) in down \
                      if (0 <= (row + x) < length) \
                          and (0 <= (col + y) < length) \
                          and board[row + x][col + y] == 1]
        
        top = [deindexify(row + x, col + y) for (x, y) in up \
                   if (0 <= (row + x) < length) \
                       and (0 <= (col + y) < length) \
                       and board[row + x][col + y] == 1]
        
        return (sorted(bottom + top) if (piece == 4 or piece == 5) else \
                (sorted(top) if (piece == 3 or piece == 5) else sorted(bottom))) \
                    if is_sorted else (bottom + top if (piece == 4 or piece == 5) else \
                                       (top if (piece == 3 or piece == 5) else bottom))
    return []

def apply_move(board, move):
    """
Performs actual operations and moves that move the specified pieces.
    use the if and piece and board class
No return
    
    Raise this exception below:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.") 
    If,
        a. there is no move from move[0], i.e. use tools.get_moves() function
        to get all the moves from move[0]
        b. the destination position move[1] is not in the moves list found
            from tools.get_moves() function.            
    """
    row,col = indexify(move[0])
    row_end,col_end = indexify(move[1])
    path_list = get_moves(board, row, col, is_sorted = False)
    
    if move[1] in path_list:
        piece = board[row][col]
        if (piece == 2 or piece == 4) and row_end == 7 \
        or (piece == 3 or piece == 5) and row_end == 0:
            piece = 5 if piece == 3 else 4
        board[row][col] = 1
        board[row_end][col_end] = piece
    else:
        raise RuntimeError("Invalid move, please type" \
                         + " \'hints\' to get suggestions.")

while running:
    board = brd.createBoard()
    move = ai.get_next_move(board, turn) # This shit causes bug, if not written here! There is import problem in ai.
    game , bot = drw.drawMenu(screen)

    while game:
        drw.drawBoard(board, screen)
        brd.printBoard(board)
        if turn == 2 and bot == 1:
            move = ai.get_next_move(board, turn)
            if type(move) == list:
                apply_capture(board, move)
            if type(move) == tuple:
                apply_move(board, move)

            print("\t{} played {}.".format(turn, str(move)))
            turn = 3
            continue

        slcrow, slccol, isKing = io.getPiece(board, turn)
        drw.highliteSquare(screen, slcrow, slccol)
        dstrow, dstcol, deslc = io.getSquare(board, turn, slcrow, slccol, isKing)

        if deslc:
            continue

        board, contAttack = brd.updateBoard(board, turn, slcrow, slccol, dstrow, dstcol)
        drw.playSound()

        if contAttack:
            continue
 
        game, winner = brd.isFinish(board, running)
        print(game)
        drw.drawFinish(screen, winner)

    

        print("========================")

        if (turn == 3) and game != False:
            turn = 2
            print("White's turn")

        elif game != False:
            turn = 3
            print("Black's turn")
drw.quit()
