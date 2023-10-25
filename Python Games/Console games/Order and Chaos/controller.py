from Domain.Board import ValidateMove, Board
from Repository.repo import Repo
import random


class Controller:
    def __init__(self, repo: Repo, validator: ValidateMove, board: Board):
        self._repo = repo
        self._validator = validator
        self._board = board

    def make_a_move(self,board: Board, row, col, symbol):
        self._validator.validate(row, col , board)
        self._repo.update(board, row, col ,symbol)

    def random_move(self, board: Board, symbol):
        ok = 0
        while ok == 0:
            row = random.randint(0,5)
            col = random.randint(0,5)
            if board.get(row,col) is None:
                ok = 1
        self.make_a_move(board, row, col, symbol)

    def verify_full(self, board):
        #Returns 1 if the board is full and 0 otherwise
        nr = 0
        for row in range(6):
            for col in range(6):
                if board.get(row, col) != None:
                    nr += 1
        if nr == 36:
            return 1
        else:
            return 0

    def save_file(self, file_name, board):
        self._repo.save_file(file_name, board)

    def load_file(self, file_name):
        board = self._repo.load_file(file_name)
        return board


