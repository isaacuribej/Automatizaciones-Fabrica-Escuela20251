Feature: Notificación de promociones

  Historia: HU008 - Notificación personalizada de promociones
    Scenario: Configuración de notificaciones
      Given que soy un cliente autenticado
      When accedo a la configuración de notificaciones en mi perfil
      Then debo activar o desactivar las notificaciones de ofertas y actualizaciones

    Scenario: Selección de medio de comunicación
      Given que soy un cliente autenticado
      When configuro mis preferencias de comunicación
      Then debo seleccionar entre diferentes medios para recibir notificaciones
      And las notificaciones deben enviarse por el medio seleccionado
