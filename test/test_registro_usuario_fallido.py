# tests/test_registro_usuario_fallido.py

from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.register_user import RegisterUser
from screenplay.questions.mensaje_validacion_campo import MensajeDeValidacionCampo

import time

def test_registro_usuario_fallido(page: Page, base_url):
    actor = Actor("UsuarioIncompleto").can(BrowseTheWeb.using(page, base_url))

    datos_usuario = {
        "id": "1122334455",
        "nombre": "Ana",
        "apellido": "García",
        "direccion": "",  # Campo vacío a propósito
        "celular": "3101234567",
        "correo": "anagarcia@test.com",
        "contrasena": "ana1234"
    }

    print("💡 Rellenando formulario...")
    actor.attempts_to(
        RegisterUser.con_datos(datos_usuario)
    )

    time.sleep(3)  # 👈 Espera 3 segundos antes de la validación

    print("🔍 Verificando mensaje de validación...")
    MensajeDeValidacionCampo.debe_mostrar("Dirección", "Completa este campo").answered_by(actor)

    time.sleep(2)  # 👈 Espera final para ver resultado antes de cerrar
