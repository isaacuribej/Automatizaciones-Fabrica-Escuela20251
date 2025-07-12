# tests/test_modificar_nombre.py

import pytest
from playwright.sync_api import Page

from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login
from screenplay.tasks.ir_a_datos_personales import IrADatosPersonales
from screenplay.tasks.modificar_nombre import ModificarNombre
from screenplay.questions.mensaje_flotante import MensajeFlotante

def test_editar_nombre_correctamente(page: Page):
    actor = Actor("User").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        Login.with_credentials("alejandroorrego@gmail.com", "user"),
        IrADatosPersonales(),
        ModificarNombre.a("Alejandro")
    )

    MensajeFlotante.debe_mostrar("¡Perfil actualizado exitosamente!").answered_by(actor)
