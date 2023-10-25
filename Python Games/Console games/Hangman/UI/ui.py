from Controller.Controller import Controller
from Domain.Sentence import Sentence


class UI:
    def __init__(self, controller: Controller):
        self._controller = controller

    def menu(self):
        print("1. Add sentence\n"
              "2. Start a game")
        self._controller.random_sentences()
        while True:
            print()
            option = input("Select option: ")
            option = option.strip()
            if option == "1":
                sentence = input("Please enter your sentence: ")
                if sentence is None:
                    print("Too short sentence!")
                else:
                    try:
                        words = sentence.split(" ")
                        ok = 1                 #to validate each word
                        for word in words:
                            if len(word)<3:
                                print("Each word must have at least 3 letters!")
                                ok = 0
                                break
                        if ok == 1:
                            new_sen = []
                            for word in words:
                                for letter in word:
                                    new_sen.append(letter)
                                new_sen.append(" ")
                            new_sen.pop()
                            self._controller.add_sen(new_sen)
                    except ValueError as ve:
                        print(str(ve))
            elif option == "2":
                the_sen = self._controller.select_sen()
                sen = []
                sen = self._controller.hangman_style(the_sen)
                #print(the_sen)
                #print(sen)
                game = Sentence(the_sen, sen ,None, None)
                print(game)
                winner = None
                the_hang=game.the_hang
                hang=game.hang

                while winner is None:

                    while True:
                        letter=input("Enter a letter: ")
                        if len(letter)!=1:
                            print("Invalid letter")
                        else:
                            nr = ord(letter)
                            if nr<97 or nr>122:
                                print("Invalid letter!")
                            else:
                                break
                    sen,ok =self._controller.update_sen(the_sen ,sen,letter)
                    if ok==0:
                        self._controller.update_hang(the_hang, hang)
                    winner =self._controller.winner(sen, hang)
                    print()
                    print(game)
                    print()

                if winner == "human":
                    print("Yaaaay You've won!")
                elif winner == "computer":
                    print("Bruh... Computer has won:((")

            else:
                print("Invalid option")









