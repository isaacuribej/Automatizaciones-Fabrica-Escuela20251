# tests/test_revisar_pedidos.py

import re
from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.login import Login
from screenplay.tasks.ir_a_mis_compras import IrAMisCompras
from screenplay.tasks.abrir_pedido import AbrirPedido

def test_revisar_pedido_especifico(page: Page):
    actor = Actor("User").can(BrowseTheWeb.using(page, base_url))

    actor.attempts_to(
        Login.with_credentials("alejandroorrego@gmail.com", "user"),
        IrAMisCompras(),
        AbrirPedido.con_guia("GU001014")  # Ajusta si la guía cambia dinámicamente
    )

    page = actor.ability_to(BrowseTheWeb).get_page()
    assert page.get_by_text("Detalles del pedido").is_visible()
