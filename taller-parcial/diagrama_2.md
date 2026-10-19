```mermaid
flowchart TD
    A([Inicio]) --> B[Imprimir: 'SISTEMA DE COBRO DE LA SALA DE JUEGOS']
    B --> C[turno = 'next']
    
    C --> D{¿turno.lower == 'next'?}
    
    D -- No --> V[/Mostrar: '¡Gracias por usar nuestro sistema!'/]
    V --> W([Fin])
    
    D -- Sí --> E[total_pagar = 0\ncantidad_personas = 0\ncontinuar_grupo = 'si']
    
    E --> F{¿continuar_grupo.lower == 'si'?}
    
    F -- Sí --> G[/Leer edad de la persona/]
    
    G --> H{¿edad < 5?}
    
    H -- Sí --> I[precio = 0\nImprimir: 'Entrada gratis ($0)']
    H -- No --> J{¿edad <= 18?}
    
    J -- Sí --> K[precio = 6\nImprimir: 'Precio de la entrada: $6']
    J -- No --> L[precio = 12\nImprimir: 'Precio de la entrada: $12']
    
    I --> M[total_pagar = total_pagar + precio\ncantidad_personas = cantidad_personas + 1]
    K --> M
    L --> M
    
    M --> N[/Preguntar: ¿Hay otra persona en este grupo? si/no/]
    N --> O[Guardar respuesta en 'continuar_grupo']
    O --> F
    
    F -- No --> P[/Imprimir Resumen de Cobro/]
    P --> Q[/Mostrar cantidad_personas/]
    Q --> R[/Mostrar total_pagar/]
    R --> S[/Preguntar: Escribe 'next' o cualquier tecla para salir/]
    S --> T[Guardar respuesta en 'turno']
    T --> D