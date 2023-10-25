from domain.board import PlayerBoard
from myException import MyException
from services.services import Services


class UI:
    def __init__(self, services: Services):
        self._services = services

    def menu(self):
        board = PlayerBoard()

        self._services.place_E(board)
        self._services.place_stars(board)
        self._services.place_B(board)
        print(board)

        while True:
            command = input("Enter command: ")
            if not command:
                print ("Invalid command")
                continue
            command = command.split(" ")

            if command[0]=="warp":
                try:
                    if len(command)!=2:
                        print("Invalid command!")
                        continue
                    if len(command[1])!=2:
                        print("Invalid command!")
                        continue
                    self._services.warp(command[1][0], command[1][1], board)
                    print(board)
                except ValueError as ve:
                    print(str(ve))
                except MyException as me:
                    print(str(me))
            elif command[0] == "savefile":
                try:
                    self._services._repo.save_file("file.txt", board)
                except IOError as io:
                    print(str(io))
                except ValueError as ve:
                    print(str(ve))
            elif command[0]=="loadfile":
                try:
                    board = self._services._repo.load_file("file.txt")
                    print(board)
                except IOError as io:
                    print(str(io))
                except ValueError as ve:
                    print(str(ve))
            else:
                print("Invalid command!")