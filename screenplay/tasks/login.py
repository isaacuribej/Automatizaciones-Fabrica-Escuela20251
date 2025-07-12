# screenplay/tasks/login.py
import screenplay
from screenplay.abilities.browse_the_web import BrowseTheWeb

class Login:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

    @staticmethod
    def with_credentials(email: str, password: str):
        return Login(email, password)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()

        page.goto("https://courier-sync.vercel.app/")
        page.get_by_role("textbox", name="Correo electrónico o usuario").fill(self.email)
        page.get_by_role("textbox", name="Contraseña").fill(self.password)
        page.get_by_role("button", name="Inicia Sesión").click()
