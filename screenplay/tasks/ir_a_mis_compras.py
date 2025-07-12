# screenplay/tasks/ir_a_mis_compras.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class IrAMisCompras:
    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        page.get_by_role("link", name="Mis compras").click()
