# tests/test_login_usuario.py

import pytest
from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login

def test_login_usuario(page: Page):
    actor = Actor("User").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        Login.with_credentials("alejandroorrego@gmail.com", "user")  # Credenciales válidas
    )

    # Verificación simple: verifica que aparece una sección privada
    page = actor.ability_to(BrowseTheWeb).get_page()
    assert page.get_by_role("link", name="Datos personales").is_visible()
