# tests/test_registro_usuario_fallido.py

from playwright.sync_api import Page
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.register_user import RegisterUser
from screenplay.questions.mensaje_validacion_campo import MensajeDeValidacionCampo

def test_registro_falla_sin_direccion(page: Page):
    actor = Actor("UsuarioIncompleto").can(BrowseTheWeb.using(page))

    datos_usuario = {
        "id": "1122334455",
        "nombre": "Ana",
        "apellido": "García",
        "direccion": "",  # Campo vacío a propósito
        "celular": "3101234567",
        "correo": "anagarcia@test.com",
        "contrasena": "ana1234"
    }

    actor.attempts_to(
        RegisterUser.con_datos(datos_usuario)
    )

    MensajeDeValidacionCampo.debe_mostrar("Dirección", "Rellene este campo.").answered_by(actor)
