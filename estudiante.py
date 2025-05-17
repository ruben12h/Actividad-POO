class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def presentarse(self):
        return (f"hola mi nombre es {self.nombre}, tengo {self.edad} años y estudio {self.carrera}")

estudiante1 = Estudiante("andres", 22, "ingenieria de sistemas")
estudiante2 = Estudiante("laura", 21, "matematicas")
print(estudiante1.presentarse())
print(estudiante2.presentarse())

