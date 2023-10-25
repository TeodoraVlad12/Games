from domain.board import Validator
from repo.repo import Repo
from services.services import Services
from ui.ui import UI

repo = Repo(None)
validator = Validator()
services = Services(repo, None, validator)
ui=UI(services)
ui.menu()