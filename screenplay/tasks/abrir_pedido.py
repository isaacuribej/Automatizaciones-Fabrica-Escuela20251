# screenplay/tasks/abrir_pedido.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class AbrirPedido:
    def __init__(self, id_guia: str):
        self.id_guia = id_guia

    @staticmethod
    def con_guia(id_guia: str):
        return AbrirPedido(id_guia)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        selector = f"button:has-text('{self.id_guia}')"
        page.get_by_role("button", name=re.compile(self.id_guia)).click()
