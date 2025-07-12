# screenplay/tasks/register_user.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class RegisterUser:
    def __init__(self, data: dict):
        self.data = data

    @staticmethod
    def con_datos(data: dict):
        return RegisterUser(data)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        page.goto("https://courier-sync.vercel.app/")
        page.get_by_role("button", name="Regístrate").click()

        page.get_by_role("textbox", name="Número de identificación").fill(self.data["id"])
        page.get_by_role("textbox", name="Nombre").fill(self.data["nombre"])
        page.get_by_role("textbox", name="Apellido").fill(self.data["apellido"])
        page.get_by_role("textbox", name="Dirección").fill(self.data["direccion"])
        page.get_by_role("textbox", name="Número de celular").fill(self.data["celular"])
        page.get_by_role("textbox", name="Correo electrónico", exact=True).fill(self.data["correo"])
        page.get_by_role("textbox", name="Confirmar correo electrónico").fill(self.data["correo"])
        page.get_by_role("textbox", name="Contraseña", exact=True).fill(self.data["contrasena"])
        page.get_by_role("textbox", name="Confirmar contraseña").fill(self.data["contrasena"])
        page.get_by_role("button", name="Registrarse").press("Enter")
