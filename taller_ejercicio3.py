# Ejercicio 3: Subcadenas ordenadas por longitud
def mostrar_subcadenas():
    palabra = input("Introduce una palabra (ej. rum): ").strip()
    subcadenas = []
    
    n = len(palabra)
    # Generar todas las subcadenas posibles
    for longitud in range(1, n + 1):
        for i in range(n - longitud + 1):
            subcadenas.append(palabra[i:i + longitud])
            
    # Ordenar por longitud de menor a mayor
    subcadenas.sort(key=len)
    
    print("\nSubcadenas ordenadas por longitud:")
    for sub in subcadenas:
        print(sub)

if __name__ == "__main__":
    mostrar_subcadenas()