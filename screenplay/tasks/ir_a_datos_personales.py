# screenplay/tasks/ir_a_datos_personales.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class IrADatosPersonales:
    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        page.get_by_role("link", name="Datos personales").click()
        page.get_by_role("button", name="Editar perfil").click()
