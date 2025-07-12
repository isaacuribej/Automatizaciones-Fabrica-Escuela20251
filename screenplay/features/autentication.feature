Feature: Autenticación y autorización

  Historia: HU001 - Acceso a perfil de cliente
    Como cliente
    Quiero acceder de forma segura a mi perfil y datos personales
    Para consultar mis envíos e historial

    Scenario: Acceso exitoso al perfil
      Given que soy un cliente registrado en el aplicativo
      When ingreso mi correo y contraseña correctos
      Then debo acceder a mi perfil personal
      And debo ver únicamente información relacionada a mi cuenta
      And puedo consultar mi historial de envíos

    Scenario: Intento de acceso con credenciales incorrectas
      Given que soy un cliente registrado en el aplicativo
      When ingreso credenciales incorrectas
      Then debo ver un mensaje de error
      And no debo acceder a mi perfil

  Historia: HU011 - Acceso a perfil de agente y administrador
    Scenario: Acceso exitoso como agente
      Given que soy un agente registrado en el sistema
      When ingreso mi correo y contraseña correctos
      Then debo acceder a mi perfil de agente
      And debo tener acceso únicamente a las secciones autorizadas para mi rol

    Scenario: Intento de acceso sin iniciar sesión
      Given que soy un agente
      When intento acceder a secciones protegidas sin iniciar sesión
      Then debo ser redirigido automáticamente a la pantalla de inicio de sesión
