Feature: Gestión de pedidos

  Historia: HU006 - Edición de información de pedido
    Scenario: Edición exitosa de un pedido no despachado
      Given que soy un cliente autenticado
      And tengo un pedido que aún no ha sido despachado
      When edito la información de dirección o encargado
      And confirmo los cambios
      Then el sistema debe actualizar la información del pedido
      And debo recibir una notificación de confirmación

    Scenario: Intento de edición de pedido despachado
      Given que soy un cliente autenticado
      And tengo un pedido que ya ha sido despachado
      When intento editar la información del pedido
      Then debo ver una notificación indicando que no puedo modificar pedidos ya despachados

  Historia: HU007 - Adición de comentarios a pedidos
    Scenario: Agregar comentario válido
      Given que soy un agente autenticado
      When selecciono un pedido específico
      And el comentario tiene menos de 250 palabras
      Then el comentario debe guardarse asociado al pedido

    Scenario: Agregar múltiples comentarios
      Given que soy un agente autenticado
      And existe un pedido con comentarios previos
      When agrego un nuevo comentario al pedido
      Then el comentario debe agregarse a la lista existente de comentarios
      And todos los comentarios deben ser visibles en orden cronológico

  Historia: HU010 - Modificación de pedidos por agentes
    Scenario: Modificación exitosa de pedido despachado
      Given que soy un agente autenticado
      And existe un pedido que ya ha sido despachado pero no entregado
      When modifico el nombre del destinatario, teléfono o dirección de entrega
      Then el sistema debe actualizar la información del pedido

    Scenario: Intento de modificación de pedido entregado
      Given que soy un agente autenticado
      And existe un pedido que ya ha sido entregado
      When intento modificar la información del pedido
      Then el sistema debe mostrar un mensaje indicando que no es posible modificar pedidos entregados
