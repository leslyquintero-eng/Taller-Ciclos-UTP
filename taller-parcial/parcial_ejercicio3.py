print("MÁQUINA EMPACADORA DE ARROZ")

numero_lote = 1
bolsas_en_stock = 2 
maquina_encendida = "si"

while maquina_encendida.lower() == "si":
    print(f"\n          PROCESANDO LOTE N° {numero_lote}")
    
    # Estructura de datos para almacenar la caja (Diccionario)
    caja = {
        "lote": numero_lote,
        "capacidad_maxima": 4,
        "bolsas": []  # Lista donde se guardan las bolsas empacadas
    }
    
    while len(caja["bolsas"]) < caja["capacidad_maxima"]:
        print(f"\nEstado actual de la caja: {len(caja['bolsas'])}/{caja['capacidad_maxima']} bolsas")
        print(f"Bolsas disponibles en el depósito de la máquina: {bolsas_en_stock}")
        
        # Verificación del stock de bolsas vacías en el depósito
        if bolsas_en_stock <= 0:
            print("ATENCION: Se han acabado las bolsas en el depósito")
            rellenar = input("¿Desea rellenar el depósito con más bolsas? (si/no): ")
            
            if rellenar.lower() == "si":
                cantidad_nueva = int(input("¿Cuántas bolsas quiere agregar al depósito?: "))
                bolsas_en_stock = cantidad_nueva
                print(f"El depósito ha sido rellenado, ahora hay {bolsas_en_stock} bolsas.")
            else:
                print("La máquina no puede continuar sin bolsas.")
                maquina_encendida = "no"
                break

        # Proceso automatizado de empaque
        if bolsas_en_stock > 0:
            print("1. Verificando bolsa......, Bolsa detectada")
            print("2. Vaciando arroz en la bolsa...")
            print("3. Sellando la bolsa...")
            
            bolsas_en_stock = bolsas_en_stock - 1
            
            # Guardar el elemento en la estructura de almacenamiento
            nombre_bolsa = f"Bolsa de arroz #{len(caja['bolsas']) + 1}"
            caja["bolsas"].append(nombre_bolsa)
            
            print("4. La bolsa ha sido empacada")
            
        # Consultar si se continúa el ciclo si la caja aún no está llena
        if len(caja["bolsas"]) < caja["capacidad_maxima"] and maquina_encendida.lower() == "si":
            maquina_encendida = input("¿La máquina sigue en funcionamiento? (si/no): ")
            if maquina_encendida.lower() != "si":
                break

    # Si la caja completó su capacidad máxima
    if len(caja["bolsas"]) == caja["capacidad_maxima"]:
        print("\nLa caja está llena, Cerrando y enviando a distribución.")
        print("DATOS DE ALMACENAMIENTO DE LA CAJA:")
        print(f"Lote de la caja: {caja['lote']}")
        print(f"Contenido (Lista): {caja['bolsas']}")
        
        # Incrementar número de lote para la siguiente caja
        numero_lote = numero_lote + 1 
        
        if maquina_encendida.lower() == "si":
            maquina_encendida = input("\n¿Desea procesar la siguiente caja con la máquina? (si/no): ")

print("\nLa máquina se ha apagado. ¡Proceso finalizado!")