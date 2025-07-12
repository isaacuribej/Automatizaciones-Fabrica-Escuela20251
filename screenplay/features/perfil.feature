Feature: Actualización de perfil de cliente

  Historia: HU004 - Actualización de perfil
    Scenario: Actualización exitosa de datos
      Given que soy un cliente autenticado
      When edito mis datos de contacto como dirección o número telefónico
      And guardo los cambios
      Then mis datos deben actualizarse en el sistema
      And debo recibir una notificación confirmando los cambios

    Scenario: Validación de campos en la actualización
      Given que soy un cliente autenticado
      When intento guardar cambios con campos vacíos
      Then debo ver mensajes de error indicando los campos requeridos
      And los cambios no deben guardarse
