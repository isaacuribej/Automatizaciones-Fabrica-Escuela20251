# screenplay/tasks/dejar_nombre_vacio.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class DejarNombreVacio:
    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        campo = page.get_by_role("textbox", name="Nombre *")
        campo.fill("")  # Borrar el nombre
        page.get_by_role("button", name="Guardar Cambios").click()
