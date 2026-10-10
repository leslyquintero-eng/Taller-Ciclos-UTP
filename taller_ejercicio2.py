# Ejercicio 2: Ordenar lista con ciclos y función predeterminada
def ordenar_lista():
    lista = [2, 4, 3, 1, 6, 7, 5, 8, 9, 10][cite: 1]
    print(f"Lista original: {lista}")
    
    # Ordenamiento usando ciclos (Método Burbuja)
    lista_ciclos = lista.copy()
    n = len(lista_ciclos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_ciclos[j] > lista_ciclos[j + 1]:
                lista_ciclos[j], lista_ciclos[j + 1] = lista_ciclos[j + 1], lista_ciclos[j]
                
    print(f"Lista ordenada con ciclos (Burbuja): {lista_ciclos}")
    
    # Verificación usando la función predeterminada de Python
    lista_predeterminada = sorted(lista)
    print(f"Lista ordenada con sorted(): {lista_predeterminada}")

if __name__ == "__main__":
    ordenar_lista()