# tests/test_busqueda_pedido_admin.py

from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login_admin import LoginAdmin
from screenplay.tasks.buscar_pedido import BuscarPedido

def test_admin_busca_pedido_por_nombre(page: Page):
    actor = Actor("Admin").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        LoginAdmin.with_credentials("admin1", "admin1"),
        BuscarPedido.por("Alejandro")
    )

    page = actor.ability_to(BrowseTheWeb).get_page()
    assert page.get_by_text("Alejandro").is_visible()
