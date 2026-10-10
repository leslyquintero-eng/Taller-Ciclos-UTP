# Ejercicio 1: Heladería
def calcular_heladeria():
    print("¡Bienvenido a la heladería del sabor! 🍦")
    total_acumulado = 0.0
    
    precios_toppings = {
        "frutas": 0.50,
        "granola": 1.50,
        "oreo": 1.00,
        "brownie": 0.75
    }
    precio_base = 1.90  # Helado sin topping cuesta $1.90

    while True:
        print("\n--- Nuevo Pedido de Helado ---")
        print(f"Helado base: ${precio_base:.2f}")
        print("Toppings disponibles:")
        print("- Frutas ($0.50)")
        print("- Granola ($1.50)")
        print("- Oreo ($1.00)[cite: 1]")
        print("- Brownie ($0.75)[cite: 1]")
        print("- Ninguno")
        
        opcion = input("¿Qué topping deseas agregar? (Escribe el nombre o 'ninguno'): ").strip().lower()
        costo_pedido = precio_base
        
        if opcion in precios_toppings:
            costo_pedido += precios_toppings[opcion]
            print(f"¡Excelente elección! Has añadido topping de {opcion}.")
        elif opcion == "ninguno" or opcion == "":
            print("Un helado clásico sin toppings. ¡Sencillo y delicioso!")
        else:
            print("⚠️ Lo sentimos, no hay el topping solicitado. Se te entregará tu helado sin topping.")
            
        total_acumulado += costo_pedido
        print(f"Costo de este helado: ${costo_pedido:.2f}")
        
        continuar = input("¿Deseas registrar otro pedido? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    print(f"\n🎉 ¡Gracias por tu compra! El valor final total a pagar es de: ${total_acumulado:.2f}. ¡Vuelve pronto! 🍨")

if __name__ == "__main__":
    calcular_heladeria()