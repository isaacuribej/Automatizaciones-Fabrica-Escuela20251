# screenplay/tasks/login_admin.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class LoginAdmin:
    def __init__(self, usuario: str, contrasena: str):
        self.usuario = usuario
        self.contrasena = contrasena

    @staticmethod
    def with_credentials(usuario: str, contrasena: str):
        return LoginAdmin(usuario, contrasena)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        page.goto("https://courier-sync.vercel.app/")
        page.get_by_role("tab", name="Administrador").click()
        page.get_by_role("textbox", name="Correo electrónico o usuario").fill(self.usuario)
        page.get_by_role("textbox", name="Contraseña").fill(self.contrasena)
        page.get_by_role("button", name=re.compile("Inicia Sesión como")).click()
