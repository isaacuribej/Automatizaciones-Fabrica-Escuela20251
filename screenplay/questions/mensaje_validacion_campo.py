# screenplay/questions/mensaje_validacion_campo.py

from screenplay.abilities.browse_the_web import BrowseTheWeb

class MensajeDeValidacionCampo:
    def __init__(self, nombre_del_campo: str, mensaje_esperado: str):
        self.nombre_del_campo = nombre_del_campo
        self.mensaje_esperado = mensaje_esperado

    @staticmethod
    def debe_mostrar(nombre_del_campo: str, mensaje: str):
        return MensajeDeValidacionCampo(nombre_del_campo, mensaje)

    def answered_by(self, actor):
        page = actor.ability_to(BrowseTheWeb).get_page()
        campo = page.get_by_role("textbox", name=self.nombre_del_campo)
        handle = campo.element_handle()
        mensaje = page.evaluate("(el) => el.validationMessage", handle)
        assert mensaje == self.mensaje_esperado, f"Se esperaba '{self.mensaje_esperado}', pero fue: '{mensaje}'"
