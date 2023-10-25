from domain.board import PlayerBoard, Validator
from myException import MyException
from repo.repo import Repo
import random

class Services:
    def __init__(self, repo: Repo, board: PlayerBoard, validator: Validator):
        self._repo = repo
        self._board = board
        self._validator = validator


    def place_stars(self, board):
        nr = 0
        while nr < 6:
            row = random.randint(0,7)
            col = random.randint(0,7)
            ok = 1
            if board.get(row, col) == " ":
                if row-1 >=0 :
                    if board.get(row-1, col) == '*':
                        ok = 0
                if row + 1<= 7:
                    if board.get(row+1, col) == '*':
                        ok = 0
                if col-1 >=0 :
                    if board.get(row, col-1) == '*':
                        ok = 0
                if col+1 <= 7 :
                    if board.get(row, col+1) == '*':
                        ok = 0
                if row-1 >= 0 and col-1 >= 0:
                    if board.get(row-1, col-1) =='*':
                        ok = 0
                if row-1>=0 and col+1<=7:
                    if board.get(row-1, col+1) == '*':
                        ok = 0
                if row+1<=7 and col+1<=7:
                    if board.get(row+1, col+1) == '*':
                        ok = 0
                if row+1<=7 and col-1 >=0:
                    if board.get(row+1, col-1) =='*':
                        ok = 0
                if ok == 1:
                    board.update(row, col, '*')
                    nr += 1


    def place_E(self, board):
        nr = 0
        while nr == 0:
            row = random.randint(0,1)
            col = random.randint(0,1)
            if board.get(row, col) == " ":
                board.update(row, col, 'E')
                nr = 1

    def place_B(self,board):
        nr = 0
        while nr<3:
            row= random.randint(0,7)
            col = random.randint(0,7)
            if board.get(row, col) == " ":
                board.update(row, col, 'B')
                nr += 1

    def warp(self, row, col , board):
        for i in range(8):
            for j in range(8):
                if board.get(i, j) == 'E':
                    erow = i
                    ecol = j
        self._validator.validate_input(row, col)
        row = ord(row) - ord('A')
        col = int(col)-1
        if board.get(row, col) != " ":
            raise MyException("Cannot overwrite squares")
        self._validator.validate_warp(row, col , board)
        board.update(row, col, 'E')
        board.update(erow, ecol, " ")
        print("mor incet")
        print(erow, ecol)

'''    
    def verify_adj(self, board, row, col):
        ok = 1
        if row - 1 >= 0:
            if board.get(row - 1, col) != None:
                ok = 0

        if row + 1 <= 7:
            if board.get(row + 1, col) != None:
                ok = 0

        if col - 1 >= 0:
            if board.get(row, col - 1) != None:
                ok = 0

        if col + 1 <= 7:
            if board.get(row, col + 1) != None:
                ok = 0

        if row - 1 >= 0 and col - 1 >= 0:
            if board.get(row - 1, col - 1) != None:
                ok = 0

        if row - 1 >= 0 and col + 1 <= 7:
            if board.get(row - 1, col + 1) != None:
                ok = 0

        if row + 1 <= 7 and col + 1 <= 7:
            if board.get(row + 1, col + 1) != None:
                ok = 0

        if row + 1 <= 7 and col - 1 >= 0:
            if board.get(row+1, col-1) !=None:
                ok = 0

        return ok
'''



