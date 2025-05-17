class Estudiante:
    def __init__(self, nombre, calificaciones):
        self.nombre = nombre
        self.calificaciones = calificaciones  # Lista de números

    def calcular_promedio(self):
        if not self.calificaciones:
            print("No hay calificaciones disponibles.")
            return 0
        promedio = sum(self.calificaciones) / len(self.calificaciones)
        print(f"El promedio de {self.nombre} es: {promedio:.2f}")
        return promedio

# Ejemplo de uso
est1 = Estudiante("Sofía", [85, 90, 78])
est1.calcular_promedio()