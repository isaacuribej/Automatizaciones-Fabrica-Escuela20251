# screenplay/tasks/modificar_nombre.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class ModificarNombre:
    def __init__(self, nuevo_nombre: str):
        self.nuevo_nombre = nuevo_nombre

    @staticmethod
    def a(nuevo_nombre: str):
        return ModificarNombre(nuevo_nombre)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        input_nombre = page.get_by_role("textbox", name="Nombre *")
        input_nombre.fill("")
        input_nombre.fill(self.nuevo_nombre)
        page.get_by_role("button", name="Guardar Cambios").click()
