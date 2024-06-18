#!/usr/bin/python3

# 0 - white square, 1 - black square
# 3 - black , 5 - king
# 2 - white , 4 - king

running = True


#turn 0 means white moves, 1 means black
turn = 0

#create board
board = [
         [0, 3, 0, 3, 0, 3, 0, 3],
         [3, 0, 3, 0, 3, 0, 3, 0],
         [0, 3, 0, 3, 0, 3, 0, 3],
         [1, 0, 1, 0, 1, 0, 1, 0],
         [0, 1, 0, 1, 0, 1, 0, 1],
         [2, 0, 2, 0, 2, 0, 2, 0],
         [0, 2, 0, 2, 0, 2, 0, 2],
         [2, 0, 2, 0, 2, 0, 2, 0]]

while running:
    if turn == 0:
        print("White's turn!")
    else:
        print("Black's turn!")


    if turn == 0:
        a, b = [int(a) for a in input("Select piece: ").split()]

        #is correct piece selected
        if (board[a][b] == 2):
            c, d = [int(a) for a in input("Select square: ").split()]
            #move
            if (c == a - 1 and (d == b - 1 or d == b + 1) and board[c][d] == 1):
                board[a][b] = 1
                if c == 0:
                    board[c][d] = 4
                else:
                    board[c][d] = 2
            #attack
            elif ((c == a - 2 or c == a + 2) and board[c][d] == 1):
                #left attack
                if d == b - 2:
                    #forward
                    if c == a - 2 and (board[a-1][b-1] == 3 or board[a-1][b-1] == 5):
                        if c == 0:
                            board[c][d] = 4
                        else:
                            board[c][d] = 2
                        board[a][b] = 1
                        board[a-1][b-1] = 1
                    #back
                    elif board[a+1][b-1] == 3 or board[a+1][b-1]==5:
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a+1][b-1] = 1
                    else:
                        print("can't attack")
                        continue

                #right attack
                if d == b + 2:
                    #forward
                    if c == a - 2 and board[a-1][b+1] == 3 or board[a-1][b+1] == 5:
                        if c == 0:
                            board[c][d] = 4
                        else:
                            board[c][d] = 2
                        board[a][b] = 1
                        board[a-1][b+1] = 1
                    #back
                    elif board[a+1][b+1] == 3 or board[a+1][b+1] == 5:
                        board[c][d] = 2
                        board[a][b] = 1
                        board[a+1][b+1] = 1
                    else:
                        print("can't attack")
                        continue

                #continue attack
                if (board[c+1][d-1] == 3 or board[c+1][d-1] == 5 and board[c+2][d-2] == 1   #left bottom
                 or board[c+1][d+1] == 3 or board[c+1][d+1] == 5 and board[c+2][d+2] == 1   #right bottom
                 or board[c-1][d-1] == 3 or board[c-1][d-1] == 5 and board[c-2][d-2] == 1   #left upper
                 or board[c-1][d+1] == 3 or board[c-1][d+1] == 5 and board[c-2][d+2] == 1): #right upper
                        for i in board:
                            print(i)
                        continue
            else:
                print("can't move")
                continue


            for i in board:
                print(i)

            turn = 1
        else:
            print("Select white piece")


    elif turn == 1:
        a, b = [int(a) for a in input("Select piece: ").split()]

        #is correct piece selected
        if (board[a][b] == 1):
            c, d = [int(a) for a in input("Select square: ").split()]
            #move
            if (c == a + 1 and (d == b - 1 or d == b + 1) and board[c][d] == 0):
                board[a][b] = 0
                board[c][d] = 1
            #attack
            elif ((c == a - 2 or c == a + 2) and board[c][d] == 0):
                #left attack
                if d == b - 2:
                    #forward
                    if c == a + 2 and board[a+1][b-1] == 2:
                        if c == 7:
                            board[c][d] = 3
                        else:
                            board[c][d] = 1
                        board[a][b] = 0
                        board[a+1][b-1] = 0
                    #back
                    elif board[a-1][b-1] == 2:
                        board[c][d] = 1
                        board[a][b] = 0
                        board[a-1][b-1] = 0
                    else:
                        print("can't attack")
                        continue

                #right attack
                if d == b + 2:
                    #forward
                    if c == a + 2 and board[a+1][b+1] == 2:
                        if c == 7:
                            board[c][d] = 3
                        else:
                            board[c][d] = 1
                        board[a][b] = 0
                        board[a+1][b+1] = 0
                    #back
                    elif board[a-1][b+1] == 2:
                        board[c][d] = 1
                        board[a][b] = 0
                        board[a-1][b+1] = 0
                    else:
                        print("can't attack")
                        continue

                #continue attack
                if (board[c+1][d-1] == 2 and board[c+2][d-2] == 0   #left bottom
                 or board[c+1][d+1] == 2 and board[c+2][d+2] == 0   #right bottom
                 or board[c-1][d-1] == 2 and board[c-2][d-2] == 0   #left upper
                 or board[c-1][d+1] == 2 and board[c-2][d+2] == 0): #right upper
                    for i in board:
                        print(i)
                    continue
            else:
                print("can't move")
                continue


            for i in board:
                print(i)

            turn = 0
        else:
            print("Select black piece")

