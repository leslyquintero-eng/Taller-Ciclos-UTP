```mermaid
flowchart TD
    A([Inicio]) --> B[Imprimir Menú de Comidas rapidas]
    B --> C[Inicializar total = 0]
    C --> D[Inicializar continuar = 'si']
    
    D --> E{¿continuar == 'si'?}
    
    E -- No --> N[/Mostrar total a pagar/]
    N --> O[/Mostrar mensaje de agradecimiento/]
    O --> P([Fin])
    
    E -- Sí --> F[/Leer opción del pedido/]
    
    F --> G{¿pedido == ?}
    
    G -- '1' --> H[total = total + 30000\nImprimir: '¡Agregaste una Hamburguesa!']
    G -- '2' --> I[total = total + 14000\nImprimir: '¡Agregaste un Perro caliente!']
    G -- '3' --> J[total = total + 15000\nImprimir: '¡Agregaste una Salchipapa!']
    G -- '4' --> K[total = total + 25000\nImprimir: '¡Agregaste una Pizzeta!']
    G -- '5' --> L[total = total + 4500\nImprimir: '¡Agregaste una Gaseosa!']
    G -- Otro --> M[Imprimir: 'Mil disculpas, no tenemos de ese plato...']
    
    H --> Q[/Preguntar: ¿Desea pedir algo más? si/no/]
    I --> Q
    J --> Q
    K --> Q
    L --> Q
    M --> Q
    
    Q --> R[Guardar respuesta en variable 'continuar']
    R --> E