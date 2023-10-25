from Control.controller import Controller
from Domain.Board import Board
from exception import MyException


class UI:
    def __init__(self, controller: Controller):
        self._controller = controller

    def menu(self):
        print("1.Start new game\n"
              "2.Play old game")

        while True:
            print()
            command = input("Enter command: ")
            command = command.strip()
            if command == "1":
                board = Board()
                print(board)
                winner = None
                while winner is None:
                    print("1.Make a move\n2.Save game\n3.Exit game")
                    option = input("Enter option: ")
                    if option == "1":
                        symbol = None
                        while symbol is None:
                            s = input("Enter symbol(x/o): ")
                            if s == "x"  or s == "o":
                                symbol = s
                            if symbol == "x":
                                computer = "o"
                            else:
                                computer = "x"
                        try:
                            row = int(input("Please enter row: "))
                            col = int(input("Please enter col: "))
                            self._controller.make_a_move(board, row, col, symbol)
                            self._controller.random_move(board, computer)
                            if self._controller.verify_full(board) == 1:
                                print("Board is full! Chaos wins!")
                                break
                            print(board)
                        except MyException as me:
                            print(str(me))
                        except ValueError as ve:
                            print(str(ve))
                    elif option == "2":
                        self._controller.save_file("file.txt", board)
                    elif option == "3":
                        self._controller.save_file("file.txt", board)
                        break
            elif command == "2":
                board=self._controller.load_file("file.txt")
                print(board)
                winner = None
                while winner is None:
                    print("1. Make a move\n2.Save game\n3.Exit game")
                    option = input("Enter option: ")
                    if option == "1":
                        symbol = None
                        while symbol is None:
                            s = input("Enter symbol(x/o): ")
                            if s == "x" or s == "o":
                                symbol = s
                            if symbol == "x":
                                computer = "o"
                            else:
                                computer = "x"
                        try:
                            row = int(input("Please enter row: "))
                            col = int(input("Please enter col: "))
                            self._controller.make_a_move(board, row, col, symbol)
                            self._controller.random_move(board, computer)
                            if self._controller.verify_full(board) == 1:
                                print("Board is full! Chaos wins!")
                                break
                            print(board)
                        except MyException as me:
                            print(str(me))
                        except ValueError as ve:
                            print(str(ve))
                    elif option == "2":
                        self._controller.save_file("file.txt", board)
                    elif option == "3":
                        self._controller.save_file("file.txt", board)
                        break