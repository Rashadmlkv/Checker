class Player:
    def get_moves(board, row, col, is_sorted=False):
        down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
        length = board.get_length()
        piece = board.get(row, col)
        if piece:
            bottom = [main.deindexify(row + x, col + y) for (x, y) in down
                      if (0 <= (row + x) < length)
                      and (0 <= (col + y) < length)
                      and board.is_free(row + x, col + y)]
            top = [main.deindexify(row + x, col + y) for (x, y) in up
                   if (0 <= (row + x) < length)
                   and (0 <= (col + y) < length)
                   and board.is_free(row + x, col + y)]
            return (sorted(bottom + top) if piece.is_king() else
                    (sorted(bottom) if piece.is_black() else sorted(top))
                    if is_sorted else (bottom + top if piece.is_king() else
                    (bottom if piece.is_black() else top)))
        return []

    def get_jumps(board, row, col, is_sorted=False):
        down, up = [(+1, -1), (+1, +1)], [(-1, -1), (-1, +1)]
        length = board.get_length()
        piece = board.get(row, col)
        if piece:
            bottom = [main.deindexify(row + 2 * x, col + 2 * y) for (x, y) in down
                      if (0 <= (row + 2 * x) < length)
                      and (0 <= (col + 2 * y) < length)
                      and board.is_free(row + 2 * x, col + 2 * y)
                      and (not board.is_free(row + x, col + y))
                      and (board.get(row + x, col + y).color() != piece.color())]
            top = [main.deindexify(row + 2 * x, col + 2 * y) for (x, y) in up
                   if (0 <= (row + 2 * x) < length)
                   and (0 <= (col + 2 * y) < length)
                   and board.is_free(row + 2 * x, col + 2 * y)
                   and (not board.is_free(row + x, col + y))
                   and (board.get(row + x, col + y).color() != piece.color())]
            return (sorted(bottom + top) if piece.is_king() else
                    (sorted(bottom) if piece.is_black() else sorted(top))
                    if is_sorted else (bottom + top if piece.is_king() else
                    (bottom if piece.is_black() else top)))
        return []

    def search_path(board, row, col, path, paths, is_sorted=False):
        path.append(main.deindexify(row, col))
        jumps = get_jumps(board, row, col, is_sorted)
        if not jumps:
            paths.append(path)
        else:
            for position in jumps:
                (row_to, col_to) = main.indexify(position)
                piece = copy.copy(board.get(row, col))
                board.remove(row, col)
                board.place(row_to, col_to, piece)
                if ((piece.color() == 'black' and row_to == board.get_length() - 1) or
                    (piece.color() == 'white' and row_to == 0)) and not piece.is_king():
                    piece.turn_king()
                row_mid = row + 1 if row_to > row else row - 1
                col_mid = col + 1 if col_to > col else col - 1
                capture = board.get(row_mid, col_mid)
                board.remove(row_mid, col_mid)
                search_path(board, row_to, col_to, copy.copy(path), paths)
                board.place(row_mid, col_mid, capture)
                board.remove(row_to, col_to)
                board.place(row, col, piece)

    def get_captures(board, row, col, is_sorted=False):
        paths = []
        board_ = copy.copy(board)
        search_path(board_, row, col, [], paths, is_sorted)
        if len(paths) == 1 and len(paths[0]) == 1:
            paths = []
        return paths

    def choose_color():
        my_color = ''
        opponent_color = ''
        while True:
            my_color = input("Pick a color: ").lower()
            if my_color == 'black' or my_color == 'white':
                break
            else:
                print("Wrong color, type only 'black' or 'white', try again.")
        opponent_color = 'black' if my_color == 'white' else 'white'
        print("You are '{:s}' and your opponent is '{:s}'.".format(my_color, opponent_color))
        return (my_color, opponent_color)

