Feature: Registro de Clientes

  Historia: HU003 - Registro de nuevo cliente
    Scenario: Registro exitoso
      Given que soy un usuario no registrado
      When completo el formulario con datos válidos
      And proporciono un correo electrónico válido
      And creo una contraseña segura
      Then mi cuenta debe ser creada correctamente
      And debo recibir confirmación de registro exitoso

    Scenario: Validación de campos obligatorios
      Given que soy un usuario completando el registro
      When dejo campos obligatorios sin completar
      And intento finalizar el registro
      Then debo ver mensajes indicando los campos obligatorios faltantes
      And no debe completarse el registro

    Scenario: Validación de campos duplicados
      Given que soy un usuario completando el registro
      When ingreso un correo electrónico ya registrado
      Then debo ver un mensaje indicando que el correo ya está en uso
      And no debe completarse el registro
