from Domain.Board import Board, ValidateMove


class Repo:
    def __init__(self, board: Board):
        self._board = board


    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new_board):
        self._board = new_board

    def update(self, board: Board, row, col , symbol):
        board.update(row, col ,symbol)

    def save_file(self, file_name, board: Board):
        fout = open(file_name, "wt")
        for i in range(0,6):
            for j in range(0,6):
                a = board.get(i, j)
                if a == None:
                    a = "#"
                fout.write(a)
                fout.write(",")
            fout.write("\n")
        fout.close()

    def load_file(self, file_name):
        board = Board()
        lines = []
        try:
            fin = open(file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError as io:
            pass
        for idx, line in enumerate(lines):
            row = line.split(",")
            for i in range(6):
                a=row[i].strip()
                if a == "#":
                    a = None
                board.update(idx, i, a)
        return board