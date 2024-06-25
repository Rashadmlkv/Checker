class Piece:
    # 1- black, 2- white, 3-black king, 4- white king
    symbols = [1, 2, 3, 4]

    __is_king = False

    def __init__(self, color = 'black', is_king = False):
        self.__color = color
        self.__is_king  = is_king

    def color(self):
        return self.__color

    def is_black(self):
        return self.__color == 'black'

    def is_white(self):
        return self.__color == 'white'

    def is_king(self):
        return self.__is_king

    def turn_king(self):
        self.__is_king = True

    def turn_pawn(self):
        self.__is_king = False

