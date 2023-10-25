from texttable import Texttable

from exception import MyException


class Board:
    def __init__(self):
        self._board = []
        for i in range(6):
            self._board.append([None, None, None, None, None, None])

    def get(self, row, col):
        if row not in [0,1,2,3,4,5,6] or col not in [0,1,2,3,4,5,6]:
            raise MyException("Move outside board!")
        return self._board[row][col]

    def update(self, row, col, symbol):
        self._board[row][col] = symbol
        return self._board

    def __str__(self):
        t= Texttable()
        h = ['/']
        for i in range(1,7):
            h.append(i)
        t.header(h)
        myrow = [" "," "," "," "," "," "]
        for i in range(6):
            for j in range(6):
                if self.get(i, j) is None:
                    myrow[j]=" "
                else:
                    myrow[j]=self.get(i,j)
            t.add_row([chr(ord('A')+i)]+ myrow)
        return t.draw()




'''
    def __str__(self):
        t = Texttable()
        header=['/']
        for i in range(6):
            header.append(i)
        t.header(header)
        visible_row = [0,0,0,0,0,0]
        for row in range(6):
            for col in range(6):
                if self.get(row, col) is None:
                    visible_row[col] = ' '
                    continue
                if self.get(row, col) is not None:
                    visible_row[col] = self.get(row, col)
            t.add_row([row] + visible_row)
        return t.draw()
'''
#board=Board()
#print(board)



class ValidateMove:
    def validate(self, row, col ,board: Board):
        if row not in [0,1,2,3,4,5,6] or col not in [0,1,2,3,4,5,6]:
            raise MyException("Move outside board!")
        if board.get(row, col) is not None:
            raise MyException("Cannot overwrite squares!")
