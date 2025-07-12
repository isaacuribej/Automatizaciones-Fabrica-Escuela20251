# screenplay/questions/mensaje_error.py
import screenplay 
from screenplay.abilities.browse_the_web import BrowseTheWeb

class MensajeDeError:
    def __init__(self, texto_esperado: str):
        self.texto_esperado = texto_esperado

    @staticmethod
    def debe_mostrar(texto: str):
        return MensajeDeError(texto)

    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        elemento = page.get_by_text(self.texto_esperado)
        assert elemento.is_visible(), f"No se encontró el mensaje: '{self.texto_esperado}'"
