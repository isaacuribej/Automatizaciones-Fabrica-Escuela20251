# tests/test_registro_usuario.py

import time
from playwright.sync_api import Page
from conftest import base_url
from screenplay.actor import Actor
from screenplay.abilities.browse_the_web import BrowseTheWeb
from screenplay.tasks.register_user import RegisterUser
from screenplay.questions.mensaje_flotante import MensajeFlotante

def test_registro_usuario_exitoso(page: Page):
    actor = Actor("NewUser").can(BrowseTheWeb.using(page, base_url))

    datos_usuario = {
        "id": "987654321",
        "nombre": "Juan",
        "apellido": "Pérez",
        "direccion": "Calle 123",
        "celular": "3012345678",
        "correo": "juanperez@test.com",
        "contrasena": "test1234"
    }

    print("🧾 Completando formulario de registro...")
    actor.attempts_to(
        RegisterUser.con_datos(datos_usuario)
    )

    # 👀 Esperamos un poco para visualizar el resultado
    time.sleep(3)

    

    # 🔚 Pausa final para observar resultado antes de cerrar
    time.sleep(2)
