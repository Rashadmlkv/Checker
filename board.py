class Board():
    def __init__(self):
        self.__length = 8

        self.__board = [[None for c in range(self._length)] \
                                for r in range(self._length)]

    def get_length(self):
        return self.__length

    def get_board(self):
        return self.__board

    def is_free(self, row, col):
        return self.__board[row][col]

    def place(self, row, col, piece):
        self.__board[row][col] = piece

    def get(self, row, col):
        return self.__board[row][col]

    def remove(self, row, col):
        self.__board[row][col] = None

    def is_empty(self):
        for r in range(self.__length):
            for c in range(self.__length):
                if not self.is_free(r,c):
                    return False
        return True

    def is_full(self):
        for r in range(self.__length):
            for c in range(self.__length):
                if self.is_free(r, c):
                    return False
        return True


