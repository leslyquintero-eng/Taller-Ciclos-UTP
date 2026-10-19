print("MENÚ DE COMIDAS RAPIDAS")
print("1. Hamburguesa clásica con papas - $30000")
print("2. Perro caliente doble - $14000")
print("3. Salchipapa - $15000")
print("4. Pizzeta de pepperoni - $25000")
print("5. Gaseosa - $4500")

total = 0
continuar = "si"

while continuar == "si":
    pedido = input("\nDigite el número del plato que desea: ")
    
    if pedido == "1":
        total = total + 30000
        print("¡Agregaste una Hamburguesa clásica con papas!")
    elif pedido == "2":
        total = total + 14000
        print("¡Agregaste un Perro caliente doble!")
    elif pedido == "3":
        total = total + 15000
        print("¡Agregaste una Salchipapa!")
    elif pedido == "4":
        total = total + 25000
        print("¡Agregaste una Pizzeta de pepperoni!")
    elif pedido == "5":
        total = total + 4500
        print("¡Agregaste una Gaseosa!")
    else:
        print("Mil disculpas, no tenemos de ese plato, pero pronto lo agregaremos para complacerte.")
        
    continuar = input("¿Desea pedir algo más? (si/no): ").lower()

print("\n------------------------------------")
print("El total a pagar es: $", total)
print("¡Gracias por su compra!")
print("------------------------------------")