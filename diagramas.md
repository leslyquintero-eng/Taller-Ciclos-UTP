<<<<<<< HEAD
```mermaid
flowchart TD
    subgraph Ejercicio1 [Ejercicio 1: Heladería]
        A1[Inicio] --> B1[total_acumulado = 0.0]
        B1 --> C1{¿Desea hacer un pedido?}
        C1 -- No --> H1[Imprimir total_acumulado final]
        H1 --> I1[Fin Ejercicio 1]
        C1 -- Sí --> D1[Ingresar opción de topping]
        D1 --> E1{¿El topping existe?}
        E1 -- Sí --> F1[Sumar precio del topping + base]
        E1 -- No --> G1[Cobrar solo precio base]
        F1 --> J1[Sumar al total_acumulado]
        G1 --> J1
        J1 --> C1
    end

    subgraph Ejercicio2 [Ejercicio 2: Ordenar Lista]
        A2[Inicio] --> B2[Definir lista original]
        B2 --> C2[Copiar lista para ciclos]
        C2 --> D2[Obtener longitud n]
        D2 --> E2[Ciclo Externo: i en range n]
        E2 --> F2[Ciclo Interno: j en range n - i - 1]
        F2 --> G2{lista j > lista j+1?}
        G2 -- Sí --> H2[Intercambiar elementos]
        H2 --> I2[Siguiente j]
        G2 -- No --> I2
        I2 --> J2{¿Terminó ciclo interno?}
        J2 -- No --> F2
        J2 -- Sí --> K2{¿Terminó ciclo externo?}
        K2 -- No --> E2
        K2 -- Sí --> L2[Verificar con sorted]
        L2 --> M2[Imprimir listas ordenadas]
        M2 --> N2[Fin Ejercicio 2]
    end

    subgraph Ejercicio3 [Ejercicio 3: Subcadenas]
        A3[Inicio] --> B3[Ingresar palabra]
        B3 --> C3[subcadenas = [], n = len palabra]
        C3 --> D3[Ciclo externo: longitud de 1 a n]
        D3 --> E3[Ciclo interno: i de 0 a n - longitud]
        E3 --> F3[Extraer subcadena y agregar a lista]
        F3 --> G3{¿Terminaron las combinaciones?}
        G3 -- No --> E3
        G3 -- Sí --> H3[Ordenar subcadenas key=len]
        H3 --> I3[Ciclo: Imprimir cada subcadena]
        I3 --> J3[Fin Ejercicio 3]
    end

    subgraph Ejercicio4 [Ejercicio 4: Calificaciones]
        A4[Inicio] --> B4[Definir student_scores y student_grades vacío]
        B4 --> C4[Ciclo: Para estudiante, score en items]
        C4 --> D4{score >= 91?}
        D4 -- Sí --> E4[Grade = Outstanding]
        D4 -- No --> F4{score >= 81?}
        F4 -- Sí --> G4[Grade = Exceeds Expectations]
        F4 -- No --> H4{score >= 71?}
        H4 -- Sí --> I4[Grade = Acceptable]
        H4 -- No --> J4[Grade = Fail]
        E4 --> K4[Guardar en student_grades]
        G4 --> K4
        I4 --> K4
        J4 --> K4
        K4 --> L4{¿Más estudiantes?}
        L4 -- Sí --> C4
        L4 -- No --> M4[Imprimir student_grades]
        M4 --> N4[Fin Ejercicio 4]
    end

    subgraph Ejercicio5 [Ejercicio 5: Paseo del Borracho]
        A5[Inicio] --> B5[x = 0, y = 0, paso = 1]
        B5 --> C5{paso <= 100?}
        C5 -- No --> I5[Imprimir ubicación final x, y]
        I5 --> J5[Fin Ejercicio 5]
        C5 -- Sí --> D5[Generar dirección aleatoria 0 a 3]
        D5 --> E5{¿Dirección?}
        E5 -- 0: Arriba --> F1[y = y + 1]
        E5 -- 1: Abajo --> F2[y = y - 1]
        E5 -- 2: Izquierda --> F3[x = x - 1]
        E5 -- 3: Derecha --> F4[x = x + 1]
        F1 --> G5[Incrementar paso en 1]
        F2 --> G5
        F3 --> G5
        F4 --> G5
        G5 --> C5
    end
=======
# Diagramas de Flujo - Taller Condicionales

## Ejercicio 1
```mermaid
graph TD
    A([Inicio]) --> B[/Leer numero/]
    B --> C{numero == 30}
    C -- Si --> D[/Imprimir Ganaste un premio/]
    C -- No --> E[/Imprimir Perdiste/]
    D --> F([Fin])
    E --> F
```

## Ejercicio 2
```mermaid
graph TD
    A([Inicio]) --> B[/Leer num1, num2/]
    B --> C{num1 menor num2}
    C -- Si --> D[/Mostrar num1 es menor/]
    C -- No --> E{num2 menor num1}
    E -- Si --> F[/Mostrar num2 es menor/]
    E -- No --> G[/Mostrar son iguales/]
    D --> H([Fin])
    F --> H
    G --> H
```

## Ejercicio 3
```mermaid
graph TD
    A([Inicio]) --> B[/Leer dia/]
    B --> C{dia es lunes}
    C -- Si --> D[/Mensaje Lunes/]
    C -- No --> E{dia es viernes}
    E -- Si --> F[/Mensaje Viernes/]
    E -- No --> G{dia es sabado o domingo}
    G -- Si --> H[/Mensaje Fin de semana/]
    G -- No --> I[/Mensaje Otro dia/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 4
```mermaid
graph TD
    A([Inicio]) --> B[/Leer numero/]
    B --> C{numero menor a 0}
    C -- Si --> D[valor_absoluto = numero * -1]
    C -- No --> E[valor_absoluto = numero]
    D --> F[/Mostrar valor_absoluto/]
    E --> F
    F --> G([Fin])
```

## Ejercicio 5
```mermaid
graph TD
    A([Inicio]) --> B[/Leer anio/]
    B --> C{anio % 4 == 0 y anio % 100 != 0 O anio % 400 == 0}
    C -- Si --> D[/Imprimir Es bisiesto/]
    C -- No --> E[/Imprimir NO es bisiesto/]
    D --> F([Fin])
    E --> F
```

## Ejercicio 6
```mermaid
graph TD
    A([Inicio]) --> B[/Leer caracter/]
    B --> C{longitud distinta de 1}
    C -- Si --> D[/Mostrar error de entrada/]
    C -- No --> E{caracter es vocal}
    E -- Si --> F[/Imprimir Es vocal/]
    E -- No --> G[/Imprimir No es vocal/]
    D --> H([Fin])
    F --> H
    G --> H
```

## Ejercicio 7
```mermaid
graph TD
    A([Inicio]) --> B[/Leer numero/]
    B --> C{numero % 3 == 0 y numero % 5 == 0}
    C -- Si --> D[/Imprimir FizzBuzz/]
    C -- No --> E{numero % 3 == 0}
    E -- Si --> F[/Imprimir Fizz/]
    E -- No --> G{numero % 5 == 0}
    G -- Si --> H[/Imprimir Buzz/]
    G -- No --> I[/Imprimir No es multiplo/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 8
```mermaid
graph TD
    A([Inicio]) --> B[/Leer opcion A, B o C/]
    B --> C{opcion es A}
    C -- Si --> D[/Voto por partido rojo/]
    C -- No --> E{opcion es B}
    E -- Si --> F[/Voto por partido verde/]
    E -- No --> G{opcion es C}
    G -- Si --> H[/Voto por partido azul/]
    G -- No --> I[/Opcion invalida/]
    D --> J([Fin])
    F --> J
    H --> J
    I --> J
```

## Ejercicio 9
```mermaid
graph TD
    A([Inicio]) --> B[/Leer fecha en formato dia, DD/MM/]
    B --> C{Es dia o fecha invalida}
    C -- Si --> D[/Mostrar Error/]
    C -- No --> E{Es Lunes, Martes o Miercoles}
    E -- Si --> F{Hubo examenes}
    F -- Si --> G[/Calcular Porcentaje Aprobados/]
    F -- No --> H[Fin Nivel]
    E -- No --> I{Es Jueves}
    I -- Si --> J{Asistencia mayor a 50 por ciento}
    J -- Si --> K[/Asistio la mayoria/]
    J -- No --> L[/No asistio la mayoria/]
    I -- No --> M{Es Viernes y fecha es 1/1 o 1/7}
    M -- Si --> N[/Nuevo ciclo e ingreso total/]
    M -- No --> H
    D --> O([Fin])
    G --> O
    H --> O
    K --> O
    L --> O
    N --> O
```
>>>>>>> 59723e545cac0e30cf8a1927b25fac40e63a9292
