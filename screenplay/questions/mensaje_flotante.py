# screenplay/questions/mensaje_flotante.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class MensajeFlotante:
    def __init__(self, texto_esperado: str):
        self.texto_esperado = texto_esperado

    @staticmethod
    def debe_mostrar(texto: str):
        return MensajeFlotante(texto)

    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        mensaje = page.get_by_text(self.texto_esperado)
        assert mensaje.is_visible(), f"No se encontró el mensaje esperado: {self.texto_esperado}"
