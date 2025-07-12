# tests/test_login_admin.py

import pytest
from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login

def test_login_administrador(page: Page):
    actor = Actor("Admin").can(BrowseTheWeb.using(page, base_url))


    actor.attempts_to(
        Login.with_credentials("admin@example.com", "admin123")  # Cambia a tus datos reales
    )

    # Verifica acceso a vista de admin
    page = actor.ability_to(BrowseTheWeb).get_page()
    assert page.get_by_text("Panel de administración").is_visible()
