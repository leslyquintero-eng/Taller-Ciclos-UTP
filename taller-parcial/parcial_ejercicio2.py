print("SISTEMA DE COBRO DE LA SALA DE JUEGOS")

turno = "next"

while turno.lower() == "next":
    total_pagar = 0
    cantidad_personas = 0
    continuar_grupo = "si"

    while continuar_grupo.lower() == "si":
        print("")
        edad = int(input("Ingrese la edad de la persona: "))
        
        # Evaluar el precio de la entrada según la edad
        if edad < 5:
            precio = 0
            print("-> Entrada gratis ($0)")
        elif edad <= 18:
            precio = 6
            print("-> Precio de la entrada: $6")
        else:
            precio = 12
            print("-> Precio de la entrada: $12")
            
        # Acumular el valor y la cantidad de clientes
        total_pagar = total_pagar + precio
        cantidad_personas = cantidad_personas + 1
        
        # Preguntar si hay otra persona en el mismo grupo
        continuar_grupo = input("¿Hay otra persona en este grupo? (si/no): ")

    # Resumen del cobro por grupo
    print("\n------------------------------------")
    print("        RESUMEN DE COBRO            ")
    print("------------------------------------")
    print(f"Total de personas ingresadas: {cantidad_personas}")
    print(f"Total a pagar en conjunto: ${total_pagar}")
    print("------------------------------------")
    
    # Preguntar si se atiende a otro grupo o se finaliza el programa
    turno = input("\nEscribe 'next' para seguir con el siguiente cliente o cualquier tecla para salir: ")

print("\n¡Gracias por usar nuestro sistema!")