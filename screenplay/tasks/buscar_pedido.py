# screenplay/tasks/buscar_pedido.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class BuscarPedido:
    def __init__(self, texto_busqueda: str):
        self.texto_busqueda = texto_busqueda

    @staticmethod
    def por(texto: str):
        return BuscarPedido(texto)

    def perform_as(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        page.get_by_role("link", name="Pedido").click()
        campo_busqueda = page.get_by_role("textbox", name=re.compile("ID envío, guía, cliente"))
        campo_busqueda.fill(self.texto_busqueda)
        campo_busqueda.press("Enter")
