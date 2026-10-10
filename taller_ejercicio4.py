# Ejercicio 4: Calificaciones de estudiantes
def evaluar_estudiantes():
    # Base de datos de student_scores provista[cite: 1, 2]
    student_scores = {
        "Harry": 88,[cite: 2]
        "Ron": 78,[cite: 2]
        "Hermione": 95,[cite: 2]
        "Draco": 75,[cite: 2]
        "Neville": 60[cite: 2]
    }
    
    student_grades = {}
    
    for estudiante, score in student_scores.items():
        if 91 <= score <= 100:
            student_grades[estudiante] = "Outstanding"[cite: 1]
        elif 81 <= score <= 90:
            student_grades[estudiante] = "Exceeds Expectations"[cite: 2]
        elif 71 <= score <= 80:
            student_grades[estudiante] = "Acceptable"[cite: 2]
        else:
            student_grades[estudiante] = "Fail"[cite: 2]
            
    print("Diccionario 'student_scores' original:")
    print(student_scores)
    print("\nDiccionario 'student_grades' resultante:")
    print(student_grades)

if __name__ == "__main__":
    evaluar_estudiantes()