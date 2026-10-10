# Ejercicio 5: Paseo del borracho en cuadrícula Manhattan
import random

def paseo_borracho():
    x, y = 0, 0  # Posición inicial (0, 0)[cite: 2]
    print(f"Posición inicial: ({x}, {y})")
    
    # Simular 100 intersecciones[cite: 2]
    for paso in range(1, 101):
        direccion = random.randint(0, 3)  # 0: Arriba, 1: Abajo, 2: Izquierda, 3: Derecha
        if direccion == 0:
            y += 1
        elif direccion == 1:
            y -= 1
        elif direccion == 2:
            x -= 1
        elif direccion == 3:
            x += 1
            
        print(f"Paso {paso}: Movimiento hacia dirección {direccion} -> Posición: ({x}, {y})")
        
    print(f"\n📍 Ubicación final después de 100 intersecciones: ({x}, {y})")

if __name__ == "__main__":
    paseo_borracho()