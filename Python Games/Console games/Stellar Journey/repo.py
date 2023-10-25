from domain.board import PlayerBoard


class Repo:
    def __init__(self, board: PlayerBoard):
        self._board = board

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, new):
        self._board = new


    def load_file(self, file_name):
        board = PlayerBoard()
        lines = []
        try:
            fin = open(file_name, "rt")
            lines =fin.readlines()
            fin.close()
        except IOError as io:
            pass
        for idx, line in enumerate(lines):
            atr =line.split(',')
            for i in range(8):
                a=atr[i].strip()
                if a=='#':
                    board.update(idx, i, " ")
                else:
                    board.update(idx, i, a)
        return board

    def save_file(self, file_name, board: PlayerBoard):
        fout = open(file_name, "wt")
        for i in range(8):
            for j in range(8):
                a=board.get(i,j)
                if a == " ":
                    fout.write('#')
                    fout.write(',')
                else:
                    fout.write(a)
                    fout.write(',')
            fout.write("\n")
        fout.close()

