from Control.controller import Controller
from Domain.Board import ValidateMove
from Repository.repo import Repo
from ui.ui import UI

repo=Repo(None)
validator=ValidateMove()
controller=Controller(repo, validator, None)
ui=UI(controller )
ui.menu()

#fara punctele 4b) si 5
#fara teste si specificatii
#la ui daca pune o comanda random cam crapa la unele