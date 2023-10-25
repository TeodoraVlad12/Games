from texttable import Texttable

from myException import MyException


class PlayerBoard:
    def __init__(self):
        self._board = []
        for i in range(8):
            self._board.append([" ", " "," ", " "," ", " "," ", " "])

    def get(self, row, col):
        if row not in [0,1,2,3,4,5,6,7] or col not in [0,1,2,3,4,5,6,7]:
            raise MyException("Move outside board")
        return self._board[row][col]

    def update(self, row, col, symbol):
        self._board[row][col] = symbol
        return self._board



    def __str__(self):
        t = Texttable()
        header = ['/']
        for i in range(1,9):
            header.append(i)
        t.header(header)

        visible_row = [" "," "," "," "," "," "," "," "]
        for row in range(8):
            for col in range(8):
                if self.get(row, col) == '*':
                    visible_row[col]='*'
                    continue
                if self.get(row, col) == " ":
                    visible_row[col] = " "
                    continue
                if self.get(row, col) == 'E':
                    visible_row[col] = 'E'
                    continue
                if self.get(row, col) == 'B':
                    if row -1 >=0:
                        if self.get(row-1, col) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if row+1 <=7:
                        if self.get(row+1, col) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if col-1 >=0 :
                        if self.get(row, col-1) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if col+1 <= 7 :
                        if self.get(row, col+1) == 'E':
                            visible_row[col] = 'B'
                    if row-1 >= 0 and col-1>=0:
                        if self.get(row-1, col-1) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if row-1 >= 0 and col+1<=7:
                        if self.get(row-1, col+1) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if row+1 <=7 and col-1>=0:
                        if self.get(row+1, col-1) == 'E':
                            visible_row[col] = 'B'
                            continue
                    if row+1 <= 7 and col+1<=7:
                        if self.get(row+1, col+1) == 'E':
                            visible_row[col] = 'B'
                            continue

            t.add_row([chr(int(ord('A') + row))] + visible_row)
        return t.draw()

class Validator:
    def validate_warp(self, row, col, board):
        if row not in [0,1,2,3,4,5,6,7]:
            raise MyException("Invalid move")
        if col not in [0,1,2,3,4,5,6,7]:
            raise MyException("Invalid move")
        for i in range(8):
            for j in range(8):
                if board.get(i, j) == 'E':
                    rowE = i
                    colE = j
                    break
        ok = 0
        if rowE-colE == row - col:
            ok =1
        if rowE == row or colE == col:
            ok =1
        if ok == 0:
            raise MyException("Must be on the same row/col/diagonal!")

    def validate_input(self, row, col):
        if row not in ['A','B','C','D','E','F','G','H']:
            raise MyException("Invalid row!")
        if col not in ['1','2','3','4','5','6','7',' 8']:
            raise MyException("Invalid column!")



