# tests/test_login_invalido.py

import pytest
from playwright.sync_api import Page

from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login
from screenplay.questions.mensaje_error import MensajeDeError


def test_login_invalido(page: Page):
    actor = Actor("User").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        Login.with_credentials("alejandroorrego@gmail.com", "user1")  # Contraseña incorrecta
    )

    MensajeDeError.debe_mostrar("Credenciales de usuario incorrectas").answered_by(actor)
