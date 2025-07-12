Feature: Historial de envíos

  Historia: HU005 - Consulta de historial de envíos
    Scenario: Visualización del historial completo
      Given que soy un cliente autenticado
      When accedo a la sección de mi historial de envíos
      Then debo ver todos mis pedidos ordenados cronológicamente
      And los pedidos más recientes deben aparecer al inicio
      And cada pedido debe mostrar fecha, estado, precio, número de guía y recibo

    Scenario: Visualización de recibo
      Given que soy un cliente visualizando mi historial
      When selecciono ver el recibo de un pedido específico
      Then el recibo debe abrirse en una ventana emergente o en otro apartado
