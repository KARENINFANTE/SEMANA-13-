import random

# Definimos las ciudades y los días de la semana
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas
import random

# Definir las ciudades y los días de la semana
ciudades = ["QUITO", "LOJA", "GUAYAQUIL"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4  # Número de semanas

# Inicializamos la matriz 3D con temperaturas aleatorias
# Matriz: [ciudad][semana][día]
temperaturas = [
    [
        [random.randint(15, 30) for _ in range(len(dias_semana))]  # Temperaturas para cada día
        for _ in range(semanas)  # Temperaturas para cada semana
    ]
    for _ in range(len(ciudades))  # Temperaturas para cada ciudad
]

# Mostrar la matriz de temperaturas
print("Matriz de Temperaturas (Ciudad, Semana, Día):")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(semanas):
        print(f"  Semana {j + 1}: {temperaturas[i][j]}")

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
print("\nPromedio de Temperaturas por Ciudad y Semana:")
for i, ciudad in enumerate(ciudades):
    print(f"\n{ciudad}:")
    for j in range(semanas):
        suma_temperaturas = sum(temperaturas[i][j])  # Suma de temperaturas de la semana
        promedio = suma_temperaturas / len(dias_semana)  # Promedio de la semana
        print(f"  Semana {j + 1}: {promedio:.2f} °C")
        