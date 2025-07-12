# tests/test_modificar_nombre_fallido.py

from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login
from screenplay.tasks.ir_a_datos_personales import IrADatosPersonales
from screenplay.tasks.dejar_nombre_vacio import DejarNombreVacio
from screenplay.questions.mensaje_validacion_campo import MensajeDeValidacionCampo

def test_no_permitir_nombre_vacio(page: Page):
    actor = Actor("UserFailed").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        Login.with_credentials("alejandroorrego@gmail.com", "user"),
        IrADatosPersonales(),
        DejarNombreVacio()
    )

    MensajeDeValidacionCampo.debe_mostrar("Nombre *", "Rellene este campo.").answered_by(actor)
